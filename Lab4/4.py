def gen_prime(n):
    for x in range(1, n + 1):
        if prim(x) == 1:
            print(x)
            yield x


def prim(x):
    if x == 0 or x == 1:
        return 0
    else:
        for i in range(2, x // 2+1):
            if x % i == 0:
                return 0
    return 1


for x in gen_prime(89):
    print(x)
