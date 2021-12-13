
if __name__ == "__main__":
    with open("1-dat.txt") as data:
        prev = -1
        acc = 0
        for l in data:
            n = int(l)
            if n > prev:
                acc += 1
            prev = n

    print(acc)

    with open("1-dat.txt") as data:
        d = []
        res = []
        prev = -1

        for l in data:
            d.append(int(l))

        for i in range(len(d)-2):
            res.append(sum(d[i:i+3]))

        acc = 0
        for r in res:
            if prev != -1:
                if r > prev:
                    acc += 1
            prev = r

        print(acc)