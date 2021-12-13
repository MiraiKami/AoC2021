if __name__ == "__main__":

    with open("6-data.txt") as data:
        lanternfishes = list(map(int, data.__next__().split(",")))

    fishes = {}
    for i in range(9):
        fishes[str(i)] = 0

    for f in lanternfishes:
        fishes[str(f)] += 1

    for i in range(256):
        new_fishes = {}
        for j in range(1, 9):
            new_fishes[str(j-1)] = fishes[str(j)]
        new_fishes['6'] += fishes['0']
        new_fishes['8'] = fishes['0']
        fishes = new_fishes

    print(sum(fishes.values()))


