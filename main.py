GRID_SIZE = 9

grid = [
    [ 3, 0, 6, 5, 0, 8, 4, 0, 0 ],
    [ 5, 2, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 8, 7, 0, 0, 0, 0, 3, 1 ],
    [ 0, 0, 3, 0, 1, 0, 0, 8, 0 ],
    [ 9, 0, 0, 8, 6, 3, 0, 0, 5 ],
    [ 0, 5, 0, 0, 9, 0, 6, 0, 0 ],
    [ 1, 3, 0, 0, 0, 0, 2, 5, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 7, 4 ],
    [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ]
]

def valid_move(grid, row, column, number):
    for i in range(0, GRID_SIZE):
        if grid[row][i] == number or grid[i][column] == number:
            return False
    
    startRow = row - (row % 3)
    startColumn = column - (column % 3)

    for i in range(3):
        for j in range(3):
            if grid[startRow + i][startColumn + j] == number:
                return False

    return True

def solve(grid, row, column):
    if row == GRID_SIZE - 1 and column == GRID_SIZE:
        return True

    if column == GRID_SIZE:
        row += 1
        column = 0

    if grid[row][column] > 0:
        return solve(grid, row, column + 1)

    for number in range(1, GRID_SIZE + 1):
        if valid_move(grid, row, column, number):
            grid[row][column] = number

            if solve(grid, row, column + 1):
                return True

        grid[row][column] = 0

    return False

def print_grid(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            print(f"{grid[i][j]}", end=" ")
        print("\n")

def main():
    if solve(grid, 0, 0):
        print_grid(grid)
    else:
        print("No valid solutions found")

if __name__ == "__main__":
    main()
