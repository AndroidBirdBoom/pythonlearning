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


if __name__ == "__main__":
    c = Student()
    c.score = 60
    print("分数：", c.score)
    # c.score = 9999