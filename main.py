### Main file to simulate the Traffic Jam puzzle
### Ting Chen and Yanish Rambocus
### Lab 1 CMSC 395 Artificial Intelligence


'''
class Vehicle:

    def __init__(self, size, direction):
        self.size = size
        self.direction = direction
'''

class Grid:
    def __init__(self):
        self.grid = 6*[6*[0]]
        self.redCar = -1

def A_star(grid):
    path_cost = 0
    frontier = {}
    frontier[0] = grid
    visited = set()

    while not frontier.empty():
        node = frontier.pop(0)

        if goal_test(node):
            return solution(node)

        visited.add(node)

        for child in actions(node):
            if child not in visited or not in frontier.values():
                frontier.put((g+h, node))
            else if child in frontier.values() and :
                replace something


    return [] 

def goal_test(state, sol_col):
    return state[0][sol_col] == -1

def solution(node):
    return []

