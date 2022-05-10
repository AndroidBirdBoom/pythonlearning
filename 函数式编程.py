import time
from collections.abc import Iterator, Iterable
from functools import reduce
import functools


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


def demo_map_reduce():
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


def is_odd(n):
    return not n % 2 == 0


# 生成器，可以不断生成奇数
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


# 筛选质数
def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# 判断回数
def is_palindrome(n):
    st = str(n)
    s = int(reduce(lambda x, y: x + y, [st[len(st) - a - 1] for a in range(len(st))]))
    return s == n


def palindrome():
    n = 1
    while True:
        if is_palindrome(n):
            yield n
        n += 1


def demo_filter():
    print(list(filter(is_odd, map(int, ['1', '2', '3', '4']))))
    d = primes()
    for n in d:
        if n > 100:
            break
        else:
            print(n)

    p = palindrome()
    for n in p:
        if n < 10000:
            print(n)
        else:
            break

    a = 123
    print(str(a)[::-1])

    s = 'abcdefg'
    print(s[:-3:-1])


def by_name(t):
    return t[1]


def demo_sort():
    l = [739, 322, 3, 909, 49, 538, -1000]
    print(sorted(l, key=abs))

    ns = ['bob', 'about', 'Zoo', 'Credit']
    print(sorted(ns, key=str.lower, reverse=True))

    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(L, key=by_name, reverse=True))


def calc_sum(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def lazy_s(*args):
    return calc_sum


def count():
    l = []
    for i in range(1, 4):
        def mul():
            return i * i

        l.append(mul)
    return l


def count_r():
    l = []
    for i in range(1, 4):
        def f(i):
            def mul():
                return i * i

            return mul

        l.append(f(i))
    return l


def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x

    return fn


def createCounter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def demo_return():
    print(calc_sum(1, 2, 3, 4))

    t = lazy_sum(1, 2, 3)
    print(t())

    tt = lazy_s(14, 4, 5)
    print(tt(1, 2, 3, 4, 5))

    # 循环体中的变量变化，导致返回结果异常
    t1, t2, t3 = count()
    print(t1())
    print(t2())
    print(t3())

    l1, l2, l3 = count_r()
    print(l1())
    print(l2())
    print(l3())

    x = inc()
    print(x())
    print(x())

    L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
    print(L)


def log_t(text):
    def log(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kw):
            print("%s %s()" % (text, fun.__name__))
            return fun(*args, **kw)

        return wrapper

    return log


@log_t('ex')
def now():
    print("2022-5-1")


def wr(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kw):
        r = fun(*args, **kw)
        print("调用结果为：%d" % r)
        return r

    return wrapper


@wr
def sum(a, b):
    return a + b


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        r = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, (time.time() - start) * 1000))
        return r

    return wrapper


def logse(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kw):
        print('begin call')
        r = fun(*args, **kw)
        print('end call')
        return r

    return wrapper


@logse
@metric
def pri():
    time.sleep(0.21)


def log(text):
    def ge(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kw):
            return fun(*args, **kw)

        return wrapper

    return ge


if __name__ == "__main__":
    t = now
    t()
    print(t.__name__)  # 名字已经变了

    print(sum(1, 2))

    pri()

    print(int('1000000', base=2))

    int2 = functools.partial(int, base=2)
    print(int2('1000000'))
