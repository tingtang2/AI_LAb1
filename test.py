# Import main functionality from main
import main

# Make an intial grid by choosing one of the three grids in main.py
grid = main.Grid(main.initial_grid2)

# Run A_Star on the grid
solution = main.A_star(grid)

# Print the solution and the path cost
for state in solution[1]:
    for row in state:
        print(row)

    print("\n")

print("Path Cost", solution[0])
