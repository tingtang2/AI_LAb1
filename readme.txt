# AI_LAb1

To run file: 
    python3 test.py

To run on the different grids:
    On line 3 of test.py, change initial_grid1 to initial_grid2 or initial_grid3

Using different heuristics:
    To use a specific heuristic, in main.py comment out the unwanted heuristic

Structure of program:
    - A Grid object keeps track of the vehicles in a grid, the solution column, path cost to the grid
      grids that led to current grid. It provides methods to access information the grid holds 

    - A method A_Star runs a search on an initial grid to return the optimal solution to the goal state

    - Other methods such as actions, which provides the list of subsequent grids from a grid
      help A_Star to run

Program output:
Total number of iterations to run the search, the path to the solution and the path cost
