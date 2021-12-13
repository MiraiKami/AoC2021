
if __name__ == "__main__":
    dist = []
    with open("7-dat.txt") as data:
        points = list(map(int, data.__next__().split(",")))

    # points = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    for i, p1 in enumerate(range(max(points))):
        dist.append([])
        for p2 in points:
            # print(p1, p2, abs(p1-p2))
            dist[i].append(sum(range(abs(p1-p2)+1)))
        # print(dist[i])
        # print()

    sum_dist = [sum(d) for d in dist]

    print(min(sum_dist))