import math

import main


# ----------------- 一元二次方程解 -----------------------
def quadratic(a, b, c):
    if not isinstance(a + b + c, (int, float)):
        print("not number!")
        return
    root = b * b - 4 * a * c
    if root < 0:
        print("无解！")
        return
    if root == 0:
        print("有一对公共解")
    if root > 0:
        print("有两个不同的解")
    x1 = (-b + math.sqrt(root)) / 2 * a
    x2 = (-b - math.sqrt(root)) / 2 * a
    print("一元二次方程的解为：%f,%f" % (x1, x2))
    return x1, x2


def calc(*numbers, **center):
    s = 0
    for n in numbers:
        s += n
    print("sum = ", s)
    print("other = ", center)
    if 'city' in center:
        print("city = ", center.get('city'))


def person(age, name, *, city, code):
    print("age = %d\nname = %s\ncity = %s\ncode = %d" % (age, name, city, code))


def person(age, name, *args, city, code):
    print("age = %d\nname = %s\ncity = %s\ncode = %d" % (age, name, city, code))
    for k in args:
        print("可变参数为：", k)


def mul(*y, number):
    s = number
    for number in y:
        s *= number

    print("传入参数%s的乘积为：%d" % (y, s))


if __name__ == '__main__':
    print(abs(-133))
    quadratic(1, 10, 3)
    calc(1, 3, 4)
    list = [3, 4, 5]
    calc(*list)
    ll = (30, 40)
    calc(*ll)
    calc(*ll, city="beijing", age=18)
    # person(15,'ergou',city='北京',code = 2343)
    person(14, '王刚', 'fdf', 'fdsfsdf', 'efefefe', city='上海', code=3344)

    print("#----------------------------------------")
    mul(1,3,number=3)
