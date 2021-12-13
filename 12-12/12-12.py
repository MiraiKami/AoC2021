from collections import defaultdict


def already_two(n, visited):
    for k, v in visited.items():
        if v == 2:
            return True

    return False


def visit(n, nodes, visited, way):
    res = 0
    cpy = way.copy()
    cpy_visited = visited.copy()
    if n == "end":
        print(way)
        return 1

    if (n not in visited or not already_two(n, visited)) and n != "start":
        cpy.append(n)
        if n.islower():
            cpy_visited[n] += 1
        for neigh in nodes[n]:
            res += visit(neigh, nodes, cpy_visited, cpy)

    return res


if __name__ == "__main__":
    nodes = defaultdict(list)

    with(open("12-dat.txt")) as data:
        for line in data:
            line = line.replace("\n", "")
            a, b = line.split("-")
            nodes[a].append(b)
            nodes[b].append(a)

    acc = 0
    for n in nodes["start"]:
        visited = defaultdict(int)
        acc += visit(n, nodes, visited, [])
        print("====")
        print()

    print(acc)