from collections.abc import Iterator, Iterable
from functools import reduce


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def sub(x, y):
    return x - y


# 高阶函数
def sub_m(x, y, z, s, add, mul):
    return mul(add(x, y), z) - s


def x2(t):
    return t * t


# 转换为首字母大写
def normalize(name):
    l = list(map(str.lower, name))
    return [str.upper(x[0]) + x[1:] for x in l]


# list求积
def prod(L):
    return reduce(lambda x, y: x * y, L)


# 把字符串'123.456'转换成浮点数123.456
def str2float(s):
    index = s.index('.')
    x1 = reduce(lambda x, y: x * 10 + y, map(int, s[:index]))
    x2 = reduce(lambda x, y: x * 10 + y, map(int, s[index + 1:]))
    return x1 + x2 / (10 ** len(s[index + 1:]))


if __name__ == "__main__":
    print(sub(mul(add(1, 2), 3), 4))
    # 高阶函数调用
    print(sub_m(1, 2, 3, 4, add, mul))
    r = map(x2, [1, 2, 3])
    print(isinstance(r, Iterator))
    print(list(r))
    print(list(map(str, [1, 2, 3])))
    print(reduce(add, ['a', 'b', 'c']))
    print(reduce(add, [1, 2, 3]))
    l = ['1', '3', '5', '7', '9']
    print(int(reduce(lambda x, y: x + y, l)))

    print(normalize(['adam', 'LISA', 'barT']))
    print(sum([1, 2, 3, 4]))
    print(prod([1, 2, 3, 4]))
    print(str2float('123.4567'))
