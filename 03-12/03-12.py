def determine(arr, n):
    gamma = []
    eps = []
    for r in arr:
        if r > (n // 2):
            gamma.append(1)
            eps.append(0)
        else:
            gamma.append(0)
            eps.append(1)
    return gamma, eps

def det2(arr, n, i):
    acc_0 = 0
    acc_1 = 0
    for a in arr:
        if int(a[i]) == 1:
            acc_1 += 1
        else:
            acc_0 += 1
    print(acc_0, acc_1)
    return 1 if acc_1 >= acc_0 else 0

def det3(arr, n, i):
    acc_0 = 0
    acc_1 = 0
    for a in arr:
        if int(a[i]) == 1:
            acc_1 += 1
        else:
            acc_0 += 1

    print(acc_0, acc_1)
    return 0 if acc_0 <= acc_1 else 1

def bin_to_dec(n):
    l = len(n)-1
    acc = 0
    for i, b in enumerate(n):
        acc += 2**(l-i)*int(b)
    return acc


if __name__ == "__main__":
    res = []
    n = 0
    with open("3-dat.txt") as data:
        for i, l in enumerate(data):
            for j, c in enumerate(l):
                if c != "\n":
                    if i == 0:
                        res.append(int(c))
                    else:
                        res[j] += int(c)
            n = i + 1

        gamma_bin, eps_bin = determine(res, n)

        gamma = bin_to_dec(gamma_bin)
        eps = bin_to_dec(eps_bin)

        print(gamma*eps)

        oxy = []
        co2 = []

        ds = []

        with open("3-dat.txt") as data:
            for l in data:
                s = l.replace("\n", "")
                ds.append(s)

        most_common = det2(ds, len(ds), 0)
        least_common = det3(ds, len(ds), 0)
        print(most_common, least_common)

        oxy = list(filter(lambda x: int(x[0]) == most_common, ds))
        co2 = list(filter(lambda x: int(x[0]) == least_common, ds))

        i = 1
        while i < len(gamma_bin) and len(oxy) > 1:
            new_oxy = []
            most_sign = det2(oxy, len(oxy), i)
            for o in oxy:
                #print(i, o, most_sign)
                if int(o[i]) == int(most_sign):
                    new_oxy.append(o)
            if len(new_oxy) != 0:
                oxy = new_oxy
            i += 1

            # for o in oxy:
            #     print(o)
            print()

        i = 1
        while i < len(gamma_bin) and len(co2) > 1:
            new_co2 = []
            least_sign = det3(co2, len(co2), i)
            print(least_sign)
            for c in co2:
                if int(c[i]) == int(least_sign):
                    new_co2.append(c)
            if len(new_co2) != 0:
                co2 = new_co2
            i += 1

        print(co2)
        print(oxy)
        oxy_dec = bin_to_dec(oxy[0])
        co2_dec = bin_to_dec(co2[0])
        print(oxy_dec*co2_dec)