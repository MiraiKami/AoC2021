def flash(i, j, ocs):
    acc = 1
    for l in range(i-1, i+2):
        for c in range(j-1, j+2):
            if not (l == i and c == j) and 0 <= l < len(ocs) and 0 <= c < len(ocs[0]):
                if ocs[l][c] != 0:
                    ocs[l][c] += 1

                if ocs[l][c] >= 10:
                    ocs[l][c] = 0
                    acc += flash(l, c, ocs)

    return acc


def synchronized(ocs):
    zeros = [[o == 0 for o in oc] for oc in ocs]
    return all([all(z) for z in zeros])


if __name__ == "__main__":
    ocs = []
    with open("11-dat.txt") as data:
        for index, line in enumerate(data):
            ocs.append([])
            line = line.replace("\n", "")
            for ch in line:
                ocs[index].append(int(ch))

    lines = len(ocs)
    cols = len(ocs[0])

    acc = 0
    n = 1
    while True:
        new_ocs = ocs.copy()
        for line in range(lines):
            for col in range(cols):
                new_ocs[line][col] += 1

        for line in range(lines):
            for col in range(cols):
                if new_ocs[line][col] >= 10:
                    new_ocs[line][col] = 0
                    acc += flash(line, col, new_ocs)

        ocs = new_ocs

        if synchronized(ocs):
            break

        n += 1

    print(acc)
    print(n)


