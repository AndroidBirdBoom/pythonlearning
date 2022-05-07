from collections.abc import Iterable, Iterator


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


def split():
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


def dic():
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


def list_gen():
    L = [x * x for x in range(1, 11)]
    print(L)
    Li = [x if x == 3 else x // 2 for x in range(1, 11) if x % 3 == 0]
    print(Li)
    Lii = [a + b for a in 'ABC' for b in 'EFG']
    print(Lii)

    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [x for x in L1 if isinstance(x, str)]
    print(L2)


def odd():
    print("----1----")
    yield 1
    print("----2----")
    yield 2
    print("----3----")
    yield 4


#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
def triangles_(lines):
    l = []
    for i in range(1, lines + 1):
        if lines == 1:
            l = [1]
            yield l
        elif lines == 2:
            l = [1, 1]
            yield l
        else:
            new = []
            for j in range(i):
                if j == 0 or j == i - 1:  # 第一个和最后一个填1
                    new.append(1)
                else:
                    new.append(l[j] + l[j - 1])

            l = new
            yield l


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]


if __name__ == "__main__":

    s = (x * x for x in range(3))
    print(s)

    for n in s:
        print(n)

    print(isinstance(s, Iterable))
    print(isinstance(s, Iterator))

    o = odd()
    next(o)
    next(o)
    next(o)
    # next(0)    报错

    t = triangles_(6)
    for x in t:
        print(x)


    for x in triangles_(2):
        print(x)

    for i in range(2):
        print(i)

    n = 0
    for t in triangles():
        print(t)
        n += 1
        if n == 10:
            break
