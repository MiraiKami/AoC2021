def is_content_equal(s1, s2):
    if len(s1) != len(s2):
        return False

    acc = 0
    for c in s1:
        if c in s2:
            acc += 1

    return acc == len(s1)


def guess(digits_letter, s):
    if len(s) == 2:
        return 1

    if len(s) == 3:
        return 7

    if len(s) == 4:
        return 4

    if len(s) == 8:
        return 8

    for k, v in digits_letter.items():
        if is_content_equal(v, s):
            return k

def determine(digits_letter, s):

    if len(s) == 6 and 1 in digits_letter and 4 in digits_letter:
        nb_four = len([c for c in s if c in digits_letter[4]])
        nb_one = len([c for c in s if c in digits_letter[1]])
        if nb_four == 3 and nb_one == 2:
            return 0
        elif nb_four == 4:
            return 9
        else:
            return 6

    if len(s) == 2:
        return 1

    if len(s) == 5 and 1 in digits_letter:
        nb_one = len([c for c in s if c in digits_letter[1]])
        if nb_one == 2:
            return 3

    if len(s) == 4:
        return 4

    if len(s) == 3:
        return 7

    if len(s) == 7:
        return 8

    if len(s) == 5 and 6 in digits_letter:
        nb_six = len([c for c in s if c in digits_letter[6]])
        if nb_six == 4:
            return 2
        elif nb_six == 5:
            return 5

    return -1

if __name__ == "__main__":
    inps = []
    outps = []
    with open("8-dat.txt") as data:
    # data = [
    # "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    # "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    # "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    # "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    # "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    # "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    # "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    # "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    # "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    # "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]

        for l in data:
            inp, outp = l.replace("\n", "").split(" | ")
            inp = inp.split(" ")
            outp = outp.split(" ")
            inps.append(inp)
            outps.append(outp)

    part1 = 0
    part2 = 0

    decode = []
    for inp, outp in zip(inps, outps):
        digits = {}
        not_guessed = []
        for i in inp:
            if i not in digits:
                n = determine(digits, i)
                if n != -1:
                    digits[n] = i
                else:
                    not_guessed.append(i)

        while not_guessed:
            to_guess = not_guessed.pop(0)
            n = determine(digits, to_guess)
            if n != -1:
                digits[n] = to_guess
            else:
                not_guessed.append(to_guess)

        acc_str = ""
        for o in outp:
            g = guess(digits, o)
            if g == 1 or g == 4 or g == 7 or g == 8:
                part1 += 1
            acc_str += str(g)
        part2 += int(acc_str)

        # print()

    print("result part 1: {}".format(part1))
    print("result part 2: {}".format(part2))


