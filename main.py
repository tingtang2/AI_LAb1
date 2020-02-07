### Main file to simulate the Traffic Jam puzzle
### Ting Chen and Yanish Rambocus
### Lab 1 CMSC 395 Artificial Intelligence

import copy

DIMENSION = 6

initial_grid1 = [   [0, 0, 0, 1, 2, 2],
                    [0, 0, 0, 1, 3, 3],
                    [4, 5, 5, 5, 6, 6],
                    [4, 0, 0, 0, 0, -1],
                    [0, 0, 7, 7, 7, -1],
                    [0, 0, 0, 0, 0, 0]
                ]

initial_grid2 = [   [1, 2, 3, 4, 4, 4],
                    [1, 2, 3, 5, 5, 5],
                    [1, 2, 6, 6, 7, 7],
                    [8, 8, 0, 0, -1, 0],
                    [0, 0, 0, 0, -1, 0],
                    [0, 0, 9, 9, 0, 0]
                ]

initial_grid3 = [   [0, 0, 1, 2, 2, 2],
                    [0, 0, 1, 3, 4, 4],
                    [0, 5, 1, 3, 0, -1],
                    [6, 5, 7, 7, 7, -1],
                    [6, 5, 0, 8, 8, 8],
                    [6, 0, 0, 0, 0, 0]
                ]


class Grid:
    # Object to define a grid and use it's properties

    def __init__(self, in_grid):
       
        self.grid = in_grid
        self.vehicles = {}
        self.prevGrid = None
        self.path_cost = 0
        self.solutionColumn = None
        
        # Populate self.vehicles
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.grid[i][j] == -1:
                    self.solutionColumn = j
                if self.grid[i][j] != 0:
                    try:
                        self.vehicles[self.grid[i][j]].append((i,j))
                    except KeyError:
                        self.vehicles[self.grid[i][j]] = [(i,j)]
            
    def getSolutionColumn(self):
        return self.solutionColumn

    def getVehicles(self):
        return self.vehicles

    def getGrid(self):
        return self.grid

    def getPathCost(self):
        return self.path_cost
    
    def getPrevious(self):
        return self.prevGrid
    
    def print(self):
        for row in self.grid:
            print(row)

    # Equality of two grids based on identical grids rather than memory addresses
    def __eq__(self, grid):
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.grid[i][j] != grid.getGrid()[i][j]: 
                    return False
        return True
                
# Perform A_Star search on a grid of Traffic Jam Puzzle
def A_star(grid):

    # Set up A_star
    frontier = [(grid, 0)]
    visited = []
    i = 0
                                                                                 
    while len(frontier) > 0:

        node = None

        # Get the minimum value
        minVal = min([entry[1] for entry in frontier])
        for item in frontier:
            if item[1] == minVal:
                node = item[0]
                frontier.remove(item)
                break

        if goal_test(node):
            print("Total iterations: ", i)
            return node.getPathCost(), solution(node)

        visited.append(node.getGrid())

        for child in actions(node):

            in_frontier = False
            index = j = 0

            for front in frontier: 
                if child.getGrid() == front[0].getGrid():
                    in_frontier = True
                    index = j
                j += 1

            if (child.getGrid() not in visited) and (child.getGrid() not in [entry[0].getGrid() for entry in frontier]):
                frontier.append((child, child.getPathCost() + heuristic(child)))


            elif in_frontier and frontier[index][1] > child.getPathCost() + heuristic(child):
                del frontier[index]
                frontier.append((child, child.getPathCost() + heuristic(child)))

        i += 1


def actions(grid): 

    # List of possible subsequent grids
    grids = []

    baseGrid = grid.getGrid()

    for vehicle, coord in grid.getVehicles().items():
        #print(vehicle, coord)
        head = coord[0]
        tail = coord[-1]

        vertical = True
        #check orientation by comparing row position of head and tail
        if head[0] == tail[0]:
            vertical = False

        if vertical:
            if isValid(head[0]-1) and baseGrid[head[0]-1][head[1]] == 0:
                action = copy.deepcopy(grid)
                action.path_cost+=1
                action.prevGrid = grid

                #update grid
                action.grid[head[0]-1][head[1]] = vehicle
                action.grid[tail[0]][tail[1]] = 0

                #update vehicle dict
                action.vehicles[vehicle].pop()
                action.vehicles[vehicle].insert(0, (head[0]-1, head[1]))

                grids.append(action)

            if isValid(tail[0]+1) and baseGrid[tail[0]+1][tail[1]] == 0:
                action = copy.deepcopy(grid)
                action.path_cost+=1
                action.prevGrid = grid

                #update grid
                action.grid[tail[0]+1][tail[1]] = vehicle
                action.grid[head[0]][head[1]] = 0

                #update vehicle dict
                action.vehicles[vehicle].pop(0)
                action.vehicles[vehicle].append((tail[0]+1, tail[1]))

                grids.append(action)
        else:
            if isValid(head[1]-1) and baseGrid[head[0]][head[1]-1] == 0:
                action = copy.deepcopy(grid)
                action.path_cost+=1
                action.prevGrid = grid

                #update grid
                action.grid[head[0]][head[1]-1] = vehicle
                action.grid[tail[0]][tail[1]] = 0

                #update vehicle dict
                action.vehicles[vehicle].pop()
                action.vehicles[vehicle].insert(0, (head[0], head[1] -1))

                grids.append(action)

            if isValid(tail[1]+1) and baseGrid[tail[0]][tail[1]+1] == 0:
                action = copy.deepcopy(grid)
                action.path_cost+=1
                action.prevGrid = grid

                #update grid
                action.grid[tail[0]][tail[1]+1] = vehicle
                action.grid[head[0]][head[1]] = 0

                #update vehicle dict
                action.vehicles[vehicle].pop(0)
                action.vehicles[vehicle].append((tail[0], tail[1] +1))
                grids.append(action)
    return grids
            
# Function to determine how beneficial a subsequent grid is to solving our problem
def heuristic(subGrid):

    return spacesToGoal(subGrid)
    #return 0
    #return freeSpaces(subGrid)
    
# Function to determine how many spaces are between the red car and the solution block in the grid
def spacesToGoal(grid):
    count = 0
    
    for i in range(DIMENSION):
        if grid.getGrid()[i][grid.getSolutionColumn()] == -1:
            return i - 1
    
# Function to determine the number of free spaces between the red car and the solution block in the grid
def freeSpaces(grid):
    count = 0
    
    for i in range(DIMENSION):
        if grid.getGrid()[i][grid.getSolutionColumn()] == -1:
            for k in range(i - 1):
                if grid.getGrid()[k][grid.getSolutionColumn()] != 0:
                    count += 1
            break
    return count

def goal_test(state):
    return state.getGrid()[0][state.getSolutionColumn()] == -1

def isValid(coord):
    return coord < 6 and coord > -1

def solution(node):
    backtrack = []

    while node is not None:
        backtrack.insert(0, node.getGrid())
        node = node.getPrevious()

    return backtrack
