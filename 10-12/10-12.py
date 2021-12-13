if __name__ == "__main__":
    acc = 0
    incompletes = []

    with open("10-dat.txt") as data:
    # data = ["[({(<(())[]>[[{[]{<()<>>",
    #         "[(()[<>])]({[<{<<[]>>(",
    #         "{([(<{}[<>[]}>{[]{[(<()>",
    #         "(((({<>}<{<{<>}{[]{[]{}",
    #         "[[<[([]))<([[{}[[()]]]",
    #         "[{[{({}]{}}([{[{{{}}([]",
    #         "{<[[]]>}<{[{[{[]{()[[[]",
    #         "[<(<(<(<{}))><([]([]()",
    #         "<{([([[(<>()){}]>(<<{{",
    #         "<{([{{}}[<[[[<>{}]]]>[]]"]
        for l in data:
            openings = []
            broke = False
            for c in l:
                if c == "{" or c == "[" or c == "(" or c == "<":
                    openings.append(c)
                else:
                    last = openings.pop()
                    if c == "}" and last != "{":
                        acc += 1197
                        broke = True
                        break
                    elif c == ")" and last != "(":
                        acc += 3
                        broke = True
                        break
                    elif c == "]" and last != "[":
                        acc += 57
                        broke = True
                        break
                    elif c == ">" and last != "<":
                        acc += 25137
                        broke = True
                        break
            if not broke:
                incompletes.append(l)

    print(acc)

    scores = []
    for l in incompletes:
        openings = []
        acc = 0
        for c in l:
            if c == "{" or c == "[" or c == "(" or c == "<":
                openings.append(c)
            elif c == "}" or c == "]" or c == ")" or c == ">":
                openings.pop()

        while openings:
            to_complete = openings.pop()

            if to_complete == "(":
                acc = acc*5 + 1
            elif to_complete == "[":
                acc = acc*5 + 2
            elif to_complete == "{":
                acc = acc * 5 + 3
            elif to_complete == "<":
                acc = acc * 5 + 4

        scores.append(acc)

    scores_sorted = list(sorted(scores))
    index_midle = len(scores_sorted)//2
    print(scores_sorted[index_midle])

