from collections.abc import Iterable


# -------------- 去除字符串首位空格 ---------------

def trim(s):
    print("分割前%s_" % s)
    if len(s) == 0:
        return s
    while s[0] == ' ':
        s = s[1:]
    while s[-1] == ' ':
        s = s[:-1]

    print("分割后%s_" % s)
    return s


if __name__ == "__main__":
    trim("    hello  world ")
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print(L[:3])
    print(L[-2:])
    print(L[:4:2])
    print(L[::2])
    s = "ABCDEFG"
    print(s[:])
    print(s[:2])
    print(s[-3:-1])
    print(s[::3])
    print(s)
    s = s[:-1]
    print(s)

    d = {'a': 1, 'b': 2, 'c': 3}
    for k in d:
        print(k)

    for value in d.values():
        print(value)

    for item in d.items():
        print(item)

    for s in 'ABC':
        print(s)

    print(isinstance(d, Iterable))

    L = [x * x for x in range(1, 11)]
    print(L)
    Li = [x if x == 3 else x//2 for x in range(1, 11) if x % 3 == 0]
    print(Li)
    Lii = [a + b for a in 'ABC' for b in 'EFG']
    print(Lii)

    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [x for x in L1 if isinstance(x,str)]
    print(L2)
