import time


def check_number(number, board, mark):
    for i, line in enumerate(board):
        for j, c in enumerate(line):
            if number == c:
                mark[i][j] = True


def is_there_winner(mark):
    cs = list(zip(*mark))

    for l, c in zip(mark, cs):
        if all(l) or all(c):
            return True

    return False


def sum_unmarked(board, mark):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not mark[i][j]:
                sum += board[i][j]
    return sum


if __name__ == "__main__":
    with open("4-data.txt") as data:
        numbers = list(map(int, data.__next__().split(",")))
        boards = []
        marked = []
        i = -1
        for line in data:
            if line == "\n":
                boards.append([])
                i += 1
            else:
                boards[i].append(list(map(int, line.split())))

        marked = []
        for i, b in enumerate(boards):
            marked.append([])
            for _ in range(5):
                marked[i].append([False]*5)

        multiplier = 0
        winner = None
        for n in numbers:
            win = False
            for b, m in zip(boards, marked):
                check_number(n, b, m)
                win = is_there_winner(m)

                if win:
                    multiplier = n
                    winner = (b, m)
                    break
            if win:
                break

        print(multiplier*sum_unmarked(*winner))

        carabistouille = [0]*len(boards)

        iter_number = iter(numbers)
        while sum(carabistouille) != len(boards)-1:
            n = iter_number.__next__()
            win = False
            for i, (b, m) in enumerate(zip(boards, marked)):
                check_number(n, b, m)
                win = is_there_winner(m)

                if win:
                    carabistouille[i] = 1

        last = -1
        for i in range(len(carabistouille)):
            if carabistouille[i] == 0:
                last = i
                break

        for n in iter_number:
            check_number(n, boards[last], marked[last])
            win = is_there_winner(marked[last])

            if win:
                multiplier = n
                break

        print(multiplier * sum_unmarked(boards[last], marked[last]))
