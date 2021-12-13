def fold(axis, n, grid):
    index = 1
    vert = axis == "x"
    size_x = len(grid[0])
    size_y = len(grid)

    while ( n-index >= 0 and n+index < size_x and vert) or (n-index >= 0 and n+index < size_y):
        if vert:
            for i in range(size_y):
                grid[i][n-index] = 1 if grid[i][n+index] == 1 or grid[i][n-index] == 1 else 0
        else:
            for i in range(size_x):
                grid[n-index][i] = 1 if grid[n+index][i] == 1 or grid[n-index][i] == 1 else 0

        index += 1

    if vert:
        new_grid = []
        for l in grid:
            new_grid.append(l[:n])
        return new_grid
    else:
        return grid[:n][:]


if __name__ == "__main__":
    xs = []
    ys = []
    instructions = []

    with open("13-dat.txt") as data:
        for line in data:
            if line == "\n":
                break
            line = line.replace("\n", "")
            x, y = tuple(map(int, line.split(",")))
            xs.append(x)
            ys.append(y)

        for line in data:
            line = line.replace("\n", "")
            ax, n = line.split("=")
            ax = ax[-1]
            n = int(n)
            instructions.append((ax, n))

    size_x = max(xs)+1
    size_y = max(ys)+1

    grid = []
    for i in range(size_y):
        grid.append([])
        for j in range(size_x):
            grid[i].append(0)

    for x, y in zip(xs, ys):
        grid[y][x] = 1

    for inst in instructions:
        ax, n = inst
        grid = fold(ax, n, grid)

    print(sum([sum(g) for g in grid]))

    grid = [["#" if c == 1 else " " for c in g] for g in grid]

    for g in grid:
        print("".join(g))
