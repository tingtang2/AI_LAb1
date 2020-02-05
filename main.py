### Main file to simulate the Traffic Jam puzzle
### Ting Chen and Yanish Rambocus
### Lab 1 CMSC 395 Artificial Intelligence

from pqdict import pqdict
import copy

        

DIMENSION = 6

initial_grid1 = [[0, 0, 0, 1, 2, 2],
                [0, 0, 0, 1, 3, 3],
                [4, 5, 5, 5, 6, 6],
                [4, 0, 0, 0, 0, -1],
                [0, 0, 7, 7, 7, -1],
                [0, 0, 0, 0, 0, 0]]


class Grid:
    def __init__(self, in_grid):
        # self.vehicles: list of tuples of tuples  where the first tuples in a tuple 
        # indicates the head of the car and the last tuples the tail 
       
        self.grid = in_grid #6*[6*[0]]
        self.vehicles = {}
        self.prevGrid = None
        self.path_cost =0
        
        # Populate self.vehicles
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.grid[i][j] != 0:
                    try:
                        self.vehicles[self.grid[i][j]].append((i,j))
                    except KeyError:
                        self.vehicles[self.grid[i][j]] = [(i,j)]
            
    def getVehicles(self):
        return self.vehicles

    def getGrid(self):
#        for row in self.grid:
 #           print(row)

        return self.grid

    def getPathCost(self):
        return self.path_cost
    def getPrevious(self):
        return self.prevGrid
    
    def print(self):
        for k, v in self.vehicles.items():
            print(k, v)

def A_star(grid):
    frontier = [(grid, 0)]
    visited = []

    i = 0

    while len(frontier) > 0:
        print("iteration: ", i)

        node = None
        minVal = min([entry[1] for entry in frontier])
        for item in frontier:
            if item[1] == minVal:
                node = item[0]
                frontier.remove(item)
                break

        #node = frontier.pop()[0]

        if goal_test(node.getGrid(), 5):
            return node.getPathCost(), solution(node)

        visited.append(node.getGrid())
        print("number visited", len(visited))
        print("frontier", len(frontier))

        for child in actions(node):
            #in_visited = False
            #for visitee in visited: 
            #    if child.getGrid() == visitee:
            #        in_visited = True

            in_frontier = False
            index = 0
            j = 0
            for front in frontier: 
                if child.getGrid() == front[0].getGrid():
                    in_frontier = True
                    index = j
                j += 1

            if (child.getGrid() not in visited) and (child.getGrid() not in [entry[0].getGrid() for entry in frontier]):
                print("putting grid in frontier")
                frontier.append((child, child.getPathCost()))
            elif in_frontier and frontier[index][0].getPathCost() > child.getPathCost():
                frontier.remove(index)
                frontier.append((child, child.getPathCost()))
                print("here")
        i += 1

    return "u fucked"
def actions(grid): 

    grids = []

    baseGrid = grid.getGrid()

    for vehicle, coordinates in grid.getVehicles().items():
        #print(vehicle, coordinates)
        head = coordinates[0]
        tail = coordinates[-1]

        vertical = True
        #check orientation by comparing row position of head and tail
        if head[0] == tail[0]:
            #print("vehicle:", vehicle)
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
                #action.path.append(grid.getPath()+[baseGrid])
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
                #action.path.append(grid.getPath()+[baseGrid])
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
                #action.path.append(grid.getPath()+[baseGrid])
                action.prevGrid = grid

                #update grid
                action.grid[tail[0]][tail[1]+1] = vehicle
                action.grid[head[0]][head[1]] = 0

                #update vehicle dict
                action.vehicles[vehicle].pop(0)
                action.vehicles[vehicle].append((tail[0], tail[1] +1))

                grids.append(action)


    return grids
            
def path_cost(current, previous):
    return 0

def goal_test(state, sol_col):
    print(state[0][5])
    return state[0][5] == -1

def isValid(coord):
    return coord < 6 and coord > -1

def solution(node):
    backtrack = []

    while node != None:
        backtrack.insert(0, node.getGrid())
        node = node.getPrevious()

    return backtrack
 
g = Grid(initial_grid1)
print(A_star(g))
