import main

grid = main.Grid(main.initial_grid3)

solution = main.A_star(grid)

for state in solution[1]:
    for row in state:
        print(row)

    print("\n")

print("Path Cost", solution[0])
