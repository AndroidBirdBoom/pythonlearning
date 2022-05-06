# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def add_number(a, b):
    if not isinstance(a, (int, float)):
        print("a is not a number")
        return
    if not isinstance(b, (int, float)):
        print("b is not a number")
        return
    print("a + b = " + str(a + b))


# ---------------------- 一元二次方程解法 ---------------------------

def judge_root(a, b, c):
    return b * b - 4 * a * c


def quadratic(a, b, c):
    if not isinstance(a + b + c, (int, float)):
        print("传参不是数字！")
        return
    if judge_root(a, b, c) < 0:
        print("无解！")
        return
    if judge_root(a, b, c) == 0:
        print("有同一个解")
    if judge_root(a, b, c) > 0:
        print("有两个不同的解")
    x1 = ((-b) + math.sqrt(b * b - 4 * a * c)) / 2 * a
    x2 = ((-b) - math.sqrt(b * b - 4 * a * c)) / 2 * a
    print("一元二次方程的解为：", (x1, x2))
    return x1, x2


# ---------------------- 默认参数 ---------------------------
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s *= x
    print("%d的%d次方为：%d" % (x, n, s))


# ---------------------- 可变参数 ---------------------------
# list，tuple转化为可变参数，前面直接加*
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n

    print("cal = %d" % sum)
    return sum

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    add_number(2, 4)
    add_number("154", 52)
    quadratic(2, 3, 1)
    quadratic(1, 3, -4)
    power(4, 3)

    calc(1,2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
