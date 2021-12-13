def find_bassin(ps, curr, s=[], visited=[]):

    if curr in visited:
        return

    if ps[curr[0]][curr[1]] == 9:
        return

    if ps[curr[0]][curr[1]] == 10:
        return

    visited.append(curr)
    top = (curr[0]-1, curr[1])
    bottom = (curr[0]+1, curr[1])
    left = (curr[0], curr[1]-1)
    right = (curr[0], curr[1]+1)
    to_visit = [v for v in [top, bottom, left, right] if v not in visited]

    for v in to_visit:
        if ps[curr[0]][curr[1]] < ps[v[0]][v[1]]:
            find_bassin(ps, v, s, visited)

    s.append(1)

if __name__ == "__main__":
    points = []
    with open("9-dat.txt") as data:
    # data = ["2199943210",
    #         "3987894921",
    #         "9856789892",
    #         "8767896789",
    #         "9899965678"]

        for l in data:
            acc = [10] + [int(c) for c in l if c != "\n"] + [10]
            points.append(acc)

    points.append([10]*len(points[0]))
    points = [[10]*len(points[0])] + points

    acc = 0
    bassins = []
    for i in range(1, len(points)-1):
        for j in range(1, len(points[i])-1):
            neighbors = [points[i-1][j]] + [points[i][j-1]] + [points[i][j+1]] + [points[i+1][j]]
            # print(points[i][j])
            # print(points[i-1][j-1:j+2])
            # print([points[i][j-1]] + [points[i][j+1]])
            # print(points[i+1][j-1:j+2])
            # print(points[i][j] not in neighbors)
            # print(min(neighbors))
            # print(points[i][j] == min(neighbors))
            # print()
            if points[i][j] not in neighbors and points[i][j] < min(neighbors):
                acc += points[i][j] + 1
                s = []
                find_bassin(points, (i, j), s)
                bassins.append(sum(s))

                # print(points[i][j], acc)
            # print()

    print(acc)
    sorted_bassins = list(sorted(bassins, reverse=True))
    print(sorted_bassins)

    print(sorted_bassins[0]*sorted_bassins[1]*sorted_bassins[2])


