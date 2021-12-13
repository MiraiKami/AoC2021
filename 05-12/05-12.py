def extract_coordinates(s):
    worker = s.replace(" -> ", ",")
    return tuple(map(int, worker.split(",")))


def fill_vert(x, y1, y2, board):
    if y1 > y2:
        y1, y2 = y2, y1

    for i in range(y1, y2+1):
        board[i][x] += 1


def fill_hor(y, x1, x2, board):
    if x1 > x2:
        x1, x2 = x2, x1

    for i in range(x1, x2+1):
        board[y][i] += 1


def fill_line(x1, y1, x2, y2, board):
    if x1 == x2:
        fill_vert(x1, y1, y2, board)
    else:
        fill_hor(y1, x1, x2, board)


def fill_diag(x1, y1, x2, y2, board):
    range_x = None
    range_y = None

    if x1 > x2:
        range_x = range(x1, x2-1, -1)
    else:
        range_x = range(x1, x2+1)

    if y1 > y2:
        range_y = range(y1, y2-1, -1)
    else:
        range_y = range(y1, y2+1)

    for i,j in zip(range_y, range_x):
        board[i][j] += 1


if __name__ == "__main__":
    floor = []

    for i in range(1000):
        floor.append([0]*1000)

    with open("5-data.txt") as data:
        for line in data:
            x1, y1, x2, y2 = extract_coordinates(line)

            if x1 == x2 or y1 == y2:
                fill_line(x1, y1, x2, y2, floor)

            else:
                fill_diag(x1, y1, x2, y2, floor)

    acc = 0
    for f in floor:
        for ff in f:
            if ff >= 2:
                acc += 1

    print(acc)