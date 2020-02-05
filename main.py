### Main file to simulate the Traffic Jam puzzle
### Ting Chen and Yanish Rambocus
### Lab 1 CMSC 395 Artificial Intelligence

from pqdict import pqdict

'''
class Vehicle:

    def __init__(self, size, direction):
        self.size = size
        self.direction = direction
'''
DIMENSION = 6

grid = [[0, 0, 0, 1, 2, 2],
        [0, 0, 0, 1, 3, 3],
        [4, 5, 5, 5, 6, 6],
        [4, 0, 0, 0, 0, -1],
        [0, 0, 7, 7, 7, -1],
        [0, 0, 0, 0, 0, 0]]


class Grid:
    def __init__(self, grid):
        # self.vehicles: list of tuples of tuples  where the first tuples in a tuple 
        # indicates the head of the car and the last tuples the tail 
       
        self.grid = grid #6*[6*[0]]
        self.vehicles = {}
        
        # Populate self.vehicles
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if grid[i][j] != 0:
                    try:
                        self.vehicles[grid[i][j]].append((i,j))
                    except KeyError:
                        self.vehicles[grid[i][j]] = [(i,j)]
            
    def getCar(self, index):
        return self.vehicles[index]

    def getGrid(self):
        return grid
    
    def print(self):
        for k, v in self.vehicles.items():
            print(k, v)



def A_star(grid):
    path_cost = 0
    frontier = pqdict({0: grid})
    visited = set()

    while not frontier.empty():
        node = frontier.pop(0)

        if goal_test(node):
            return solution(node)

        visited.add(node)

        for child in actions(node):
            if child not in visited or child not in frontier.values():
                print("putting grid in frontier")

                '''
            elif child in frontier.values():
                replace something
                '''
def actions(grid): 

    grids = []

    baseGrid = grid.getGrid()
    
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            print("i: " + i)
            print("j: " + j)

            if baseGrid[i][j] != 0 and baseGrid[i][j] == baseGrid[i][j+1] == baseGrid[i][j+2]:
                if j > 0 and j < 4:
                    if baseGrid[i][j - 1] == 0:
                        newGrid = baseGrid.deepcopy()

            elif baseGrid[i][j] != 0 and baseGrid[i][j] == baseGrid[i][j+1]:
                print("elif")
            


   

def goal_test(state, sol_col):
    return state.get[0][0] == (sol_col, 0)

def solution(node):
    return []

