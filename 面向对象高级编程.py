from types import MethodType
from enum import Enum, unique


def set_score(self, score):
    self.score = score


class Student(object):
    __slots__ = ('age', '_score')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class AC(Student):
    __slots__ = ('name')


class Person(object):

    def __init__(self):
        self._age = None

    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def set_age(self, age):
        if age <= 0:
            raise Exception("不能赋负值！")
        elif age > 200:
            raise Exception("年龄不能过大！")
        else:
            self._age = age


def demo_slots():
    tom = Student()
    tom.age = "18"
    print("tom.age = ", tom.age)
    jack = Student()
    Student.set_score = set_score
    jack.set_score(50)
    print("jack.score = ", jack.score)

    sily = AC()
    sily.name = 'sily'
    print("sily.name = ", sily.name)

    sily.age = 38
    print("sily.age = ", sily.age)


class Screen(object):

    def __init__(self):
        self._width = None
        self._height = None
        self._resolution = 786432

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._resolution


def demo_property():
    c = Student()
    c.score = 60
    print("分数：", c.score)
    # c.score = 9999

    spicy = Person()
    spicy.set_age = 80
    print(spicy.get_age)


class Animal(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Mammal(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)


class Bird(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)


class FlyableMinIn(object):

    def fly(self):
        print("我会飞！")


class RunnableMinIn(object):

    def run(self):
        print("我会跑！")


class Dog(Mammal, RunnableMinIn):

    def __init__(self, name):
        Mammal.__init__(self, name)

    def to_string(self):
        print("我是：", self.name)
        RunnableMinIn.run(self)

    def __str__(self):
        return 'I am %s' % super().name

    def __repr__(self):
        return self.__str__()


class Bat(Bird, FlyableMinIn):

    def __init__(self, name):
        Bird.__init__(self, name)

    def to_string(self):
        print("我是：", self.name)
        super().fly()


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        a, b = 1, 1
        if isinstance(item, int):
            for x in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):  # 判断是不是切片
            L = []
            start = item.start
            end = item.stop
            if start is None:
                start = 0
            for n in range(end):
                if n >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    def __getattr__(self, item):
        if item == 'score':
            return 940
        elif item == 'age':
            return lambda x: x + 1


class Student(object):

    def __init__(self, name):
        self._name = name

    def __call__(self, *args, **kwargs):
        print("My name is ", self._name)


tom = Student('tom')


def demo_st():
    d = Dog('狗子')
    d.to_string()

    b = Bat('蝙蝠')
    b.to_string()

    print(Dog('狐狸'))
    print(d)

    fib = Fib()
    for f in fib:
        print(f)

    print(fib[3:7])

    print(fib.score)
    print(fib.age(2984))

    tom = Student('tom')
    tom()
    print(callable(tom))
    print(callable(b))
    print(callable([1, 2, 3]))


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


import types


def fn(self, hel):
    print("say", hel)


if __name__ == "__main__":
    print(Weekday.Mon.value)

    for name, mumber in Weekday.__members__.items():
        print(name, "=>", mumber)

    print(Weekday(1))
    print(Weekday(1) == Weekday.Mon)

    print(type(abs) == types.BuiltinFunctionType)

    Hello = type('Hello', (object,), dict(hello=fn))
    h1 = Hello()
    h1.hello('Aloha')
