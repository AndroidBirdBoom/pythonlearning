import types


class Person(object):

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def to_string(self):
        print("姓名：%s，性别：%s" % (self.__name, self.__gender))


class Student(Person):
    count = 0

    def __init__(self, name, gender, score):
        self.__score = score
        Student.count += 1

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def to_string(self):
        print("student:", self.__score)


class Animal(object):

    def to_string(self):
        print("I can really dance!")


def print_o(obj):
    obj.to_string()


class MyObject(object):
    name = 'tom'

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


if __name__ == "__main__":
    jack = Person('jack', 'female')
    tom = Student('tom', 'female', 99)

    print("tom is Student?", isinstance(tom, Student))
    print("tom is Person?", isinstance(tom, Person))

    a = Animal()

    print_o(jack)
    print_o(tom)
    print_o(a)

    print(type(a))
    print(type(jack))
    print(type(tom))
    print(type(123))

    print(type(print_o) == types.FunctionType)
    print(type(lambda x: x) == types.LambdaType)
    print(type((x for x in range(9))) == types.GeneratorType)
    print(type(lambda x: x))
    print(type(jack.to_string) == types.MethodType)

    print(dir(jack))
    print(hasattr(jack, 'gender'))

    obj = MyObject()
    print("hasattr x ?", hasattr(obj, 'x'))
    print("x = ", obj.x)
    print("setattr x = 13")
    setattr(obj, 'x', 13)
    print("x = ", obj.x)

    print("hasattr z ?", hasattr(obj, 'z'))
    print("z = ", getattr(obj, 'z', 404))

    print("hasattr power?", hasattr(obj, 'power'))
    print("call power():", getattr(obj, 'power')())

    print(obj.name)
    print(MyObject.name)
    obj.name = 'jack'
    MyObject.name = 'wawa'
    print(obj.name)
    print(MyObject.name)
    del obj.name
    print(obj.name)

    print("数量为：", Student.count)
    lihua = Student('lihua', 'gender', 48)

    print("数量为：", Student.count)
