from types import MethodType


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
        Animal.__init__(self,name)


class Bird(Animal):

    def __init__(self, name):
        Animal.__init__(self,name)


class FlyableMinIn(object):

    def fly(self):
        print("我会飞！")


class RunnableMinIn(object):

    def run(self):
        print("我会跑！")


class Dog(Mammal, RunnableMinIn):

    def __init__(self, name):
        Mammal.__init__(self,name)

    def to_string(self):
        print("我是：", self.name)
        RunnableMinIn.run(self)


class Bat(Bird, FlyableMinIn):

    def __init__(self, name):
        Bird.__init__(self,name)

    def to_string(self):
        print("我是：", self.name)
        super().fly()


if __name__ == "__main__":
    d = Dog('狗子')
    d.to_string()

    b = Bat('蝙蝠')
    b.to_string()