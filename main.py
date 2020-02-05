### Main file to simulate the Traffic Jam puzzle
### Ting Chen and Yanish Rambocus
### Lab 1 CMSC 395 Artificial Intelligence

from pqdict import pqdict
import copy

'''
class Vehicle:

    def __init__(self, size, direction):
        self.size = size
        self.direction = direction
        '''

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
        self.path = []
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
        for row in self.grid:
            print(row)

        return self.grid

    def getPath(self):
        return self.path

    def getPathCost(self):
        return self.path_cost
    
    def print(self):
        for k, v in self.vehicles.items():
            print(k, v)



def A_star(grid):
    path_cost = 0
    frontier = pqdict({grid: 0})
    visited = []

    i = 0

    while len(frontier.keys()) > 0:
        print("iteration: ", i)
        node = frontier.popitem()[0]

        if goal_test(node.getGrid(), 5):
            return node.getGrid()

        visited.append(node.getGrid())
        print("number visited", len(visited))
        print("frontier", len(frontier.items()))

        for child in actions(node):
            in_visited = False
            for visitee in visited: 
                if child.getGrid() == visitee:
                    in_visited = True

            in_frontier = False
            for front in frontier: 
                if child.getGrid() == front.getGrid():
                    in_frontier = True

            if not in_frontier or not in_visited:
                print("putting grid in frontier")
                frontier[child] = child.getPathCost()
            #elif in_frontier and frontier[child] > child.getPathCost():
            #    frontier[child] = child.getPathCost()
            #    print("here")
        i += 1
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

                #update grid
                action.grid[tail[0]][tail[1]+1] = vehicle
                action.grid[head[0]][head[1]] = 0

                #update vehicle dict
                action.vehicles[vehicle].pop(0)
                action.vehicles[vehicle].append((tail[0], tail[1] +1))

                grids.append(action)

    '''
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            print("i: " + i)
            print("j: " + j)

            if baseGrid[i][j] != 0 and baseGrid[i][j] == baseGrid[i][j+1] == baseGrid[i][j+2]:
                if j > 0 and j < 4:
                    if baseGrid[i][j - 1] == 0:
                        newGrid = baseGrid.deepcopy()

            elif baseGrid[i][j] != 0 and baseGrid[i][j] == baseGrid[i][j+1]:
                print("elif")'''

    return grids
            
def path_cost(current, previous):
    return 0

def goal_test(state, sol_col):
    return state[0][sol_col] == '-1'

def isValid(coord):
    return coord < 6 and coord > -1

def solution(node):
    return []
 
