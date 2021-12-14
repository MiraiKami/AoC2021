from collections import defaultdict


def cnt_pairs(ps, chains):
    res = defaultdict(int)
    for i, (c, v) in enumerate(ps.items()):
        if c in chains:
            res[c[0]+chains[c]] += v
            res[chains[c] + c[1]] += v
        else:
            res[c] += 1


    return res


def cnt_elem(p, ps):
    distinct_elems = set(p)
    res = defaultdict(int)
    for e, v in ps.items():
        res[e[0]] += v

    res[p[-1]] += 1

    return res


# Not efficient as it grows exponentially
def polymerize(p, chains):
    new_polymer = []
    for i in range(len(p)-1):
        chain = "".join(p[i:i+2])
        if chain in chains:
            new_polymer.append(p[i])
            new_polymer.append(chains[chain])
    new_polymer.append(polymer[-1])
    return new_polymer


if __name__ == "__main__":
    polymer = None
    pairs = {}

    with open("13-dat.txt") as data:
        polymer = [c for c in data.__next__() if c != "\n"]
        data.__next__()

        for line in data:
            line = line.replace("\n", "")
            chain, insert = line.split(" -> ")
            pairs[chain] = insert

    pair_number = defaultdict(int)
    for i in range(len(polymer)-1):
        pair_number["".join(polymer[i:i+2])] += 1

    for n in range(40):
        pair_number = cnt_pairs(pair_number, pairs)

    nb_per_elem = list(sorted(cnt_elem(polymer, pair_number).values()))
    print(abs(nb_per_elem[0]-nb_per_elem[-1]))
