
if __name__ == "__main__":
    with open("2-dat.txt") as data:
        hor = 0
        depth = 0
        for l in data:
            info = l.split()

            if info[0] == "forward":
                hor += int(info[1])

            elif info[0] == "up":
                depth -= int(info[1])

            elif info[0] == "down":
                depth += int(info[1])

        print(hor*depth)

    with open("2-dat.txt") as data:
        hor = 0
        depth = 0
        aim = 0

        for l in data:
            info = l.split()

            if info[0] == "forward":
                hor += int(info[1])
                depth += int(info[1])*aim

            elif info[0] == "up":
                aim -= int(info[1])

            elif info[0] == "down":
                aim += int(info[1])

        print(hor*depth)