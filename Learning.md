[函数](###1)

- [格式](####1)
- [返回多个值](####2)
- [函数参数](####3)
    - [可变参数](#####1)
    - [关键字参数](#####2)

[高级特性](###2)

- [切片](####21)
- [迭代](####22)
- [列表生成器](####23)
- [生成器](####24)
- [迭代器](####25)

[函数式编程](###3)

- [高阶函数](####31)
- [返回函数](####32)
- [匿名函数](####33)
- [装饰器](####34)
- [偏函数](####35)

[模块](###4)  
[面向对象编程](###5)

- [类和实例](####51)
- [访问限制](####52)
- [继承和多态](####53)
- [获取对象信息](####54)
- [实例属性和类属性](####55)

[面向对象高级编程](###6)

- [使用__slots__](####61)
- [使用@property](####62)
- [多重继承](####63)
- [定制类](####64)
    - [\_\_str__、\_\_repr__](#####641)
    - [\_\_iter__、\_\_next__](#####642)
    - [\_\_getitem__](#####643)
    - [\_\_getattr__](#####644)
    - [\_\_call__](#####645)
- [使用枚举类](####65)
- [使用元类](####66)

[错误、调试和测试](###7)

- [错误处理](####71)
    - [logging、raise](#####711)
- [调试](####72)
- [单元测试](####73)
- [文档测试](####74)

[IO编程](###8)

- [文件读写](####81)
- [StringIO和BytesIO](####82)
- [操作文件和目录](####83)
- [序列化](####84)

[正则表达式](###9)  
[常用内建模块](###10)  
[常用第三方模块](###11)

## <span id = '##1'>函数</span>

----------

### <span id = '###1'>1. 格式：

```python
def function_name(a, b):
    # 如果不加return，默认返回None.
    return 
```

### <span id = '###2'>2. 返回多个值</span>

> **python中的函数可以返回多个值**，简单来说就是返回了一个元组（tuple）

### <span id = '###3'>3. 函数参数</span>

参数分为必选参数、默认参数、可变参数、关键字参数和命名关键字参数几种
> 注意：参数的定义顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

```python
# 默认参数，且必须放在必选参数后面
def power(x, n=2, hint=""):
    return


# 默认参数可以不写
power(5, hint="备注消息")

# 默认参数也可以不按顺序，但必须明确
power(10, hint="默认参数", n=9)
```

#### <span id ='####1'>1. 可变参数</span>

> 当调用的函数参数不明确时，可以使用可变参数
> > 可变参数传入在函数中组装为一个tuple

```python
def calc(*numbers):
    s = 0
    for n in numbers:
        s += n
    print("sum = ", s)


calc(1, 3, 4)

# 也可以使用 * + list 传入list或者tuple
list = [1, 3, 4, 5]
calc(*list)

calc(1, 3, 4, 5, city="北京", age=18)
```

#### <span id ='####2'>2. 关键字参数</span>

> 1. 关键字参数视为dict
> 2. 命名关键字参数必须传入参数名，否则会调用出错

```python
def person(name, age, **center):
    # 查看center中的元素
    if 'city' in center:
        print("city = ", center.get('city'))

    # 命名关键字通过以下方式：


def person(name, age, *, code, city):
    pass


# 如果含有可变参数的话，后面的关键字可以不带*
def person(name, age, *args, city, code):
    pass


# 同样的，也可以掺杂默认参数使用
def person(name, age, *, city="北京", code):
    pass


person("hahah")
```

## <span id = '##2'>高级特性</span>

-----

### <span id ='###21'>1. 切片</span>

> 可以对list或tuple进行切片操作，一次性截取多个元素
> > 也可以对str进行切片

```python
L = ['a', 'b', 'c', 'd', 'e']

# 获取前两个元素，等同于L[0:2]
L[:2]

# 同样也可以从后面取
L[-2:]

# 取前4个数间隔为2
L[:4:2]

# 所有数每隔2个
L[::2]
```

### 2. <span id ='###22'>迭代</span>

> 可以理解为数组的遍历，但是python中不止可以遍历list/tuple，还可以遍历dict。事实上，**<font color="red">只要是可迭代对象，都可以使用for in 遍历</font>**
> > str也可以迭代

```python
from collections.abc import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

# 使用以下方法判断是否可迭代 
isinstance(d, Iterable)

# 默认遍历的是key，即a,b,c
for key in d:
    print(key)

# 遍历的是1,2,3
for value in d.values():
    print(value)

# 遍历的是('a':1)、('b':2)、('c':3)
for item in d.items():
    print(item)

for s in 'ABC':
    print(s)
```

### 3. <span id ='###23'>列表生成器</span>

> 按照一定的命令快速生成list

```python
# 下列代码生成 1*1，2*2...等值
L = []
for x in range(1, 11):
    L.append(x * x)

# 上述代码通过列表生成器实现如下：
L = [x * x for x in range(1, 11)]

# 可以在for后面加入判断语句筛选结果
L = [x * x for x in range(1, 11) if x % 2 == 0]

# 也可以使用多个for
L = [x + y for x in 'ABC' for y in 'EFG']

# 通常，可以在for 中输出多个值
d = {'a': 1, 'b': 2, 'c': 3}
L = [k + " = " + v for k, v in d.items()]

# 列表生成器后面只能有if，不能有else，而生成器前面必须是if+else
L = [x if x == 3 else x // 2 for x in range(1, 11) if x % 3 == 0] 
```

### 4. <span id ='###24'>生成器</span>

> 动态生成的一种机制，可以只在需要的时候生成
> > 比如list需要首先创建并且初始化数据，生成器只需要在需要的时候才生成数据
>
> 生成器的创建方式：
> 1. 列表生成器中的[]改为()
> 2. 函数中使用yield后，变为generator函数
     >

+ generator函数在调用next()函数时运行，遇到yield返回

> + 再次调用generator函数时，从上次yield处继续运行

```python
# 通过改变列表生成器的()产生的生成器
s = (x * 3 for x in range(10))

# 可以通过使用以下方法获取数据，但是没有数据时会产生StopIteration错误
next(s)

# 也可以通过for遍历数据，并且不会产生上述错误
for n in s:
    print(n)


# 下面是generator function，只有调用next时，才运行，运行到yield停止，除非再次调用next
# 或者利用 for 循环遍历
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]
```

### 5. <span id ='###25'>迭代器</span>

> 可以被next()调用的叫做迭代器
> > for 可以作用在两种数据类型当中
> > 1. 集合数据类型。list、tuple、dict、set、str等
> > 2. generator。生成器、generator function
>

| 数据类型  | list | tuple | dict | set | 生成器 | generator function |  
|:-----:|:----:|:-----:|:----:|:---:|:---:|:------------------:|
|Iterable| yes  |  yes  | yes  | yes | yes |        yes         |
|Iterator|no|no|no|no| yes |        yes         |

> 通过上图可知，**生成器与generator function都是Iterable，但其他未必是Iterator**，<font color="red">可以通过iter()方法将Iterable转化为Iterator</font>

```python
from collections.abc import Iterable, Iterator

t = [x for x in range(10)]  # Iterable
g = (x for x in range(10))  # Iterable & Iterator

isinstance(t, Iterable)  # True
isinstance(t, Iterator)  # False
isinstance(g, Iterable)  # True
isinstance(g, Iterable)  # True

```

## <span id = '##3'>函数式编程</span>

-------  
> 函数式编程的特点，允许把函数本身作为参数传递给另一个函数，还允许返回一个函数。

```python
# 求 (1 + 2) * 3 - 4
def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def sub(x, y):
    return x - y


sub(mul(add(1, 2), 3), 4)
```

### <span id = '###31'>1. 高阶函数</span>

> 简单理解就是函数的参数是其他的函数

```python
# map(一个函数,一个Iterable)
map(str, [1, 2, 3])  # 转换为字符型list

# reduce(一个函数，一个Iterable)
# reduce传入的函数必须接收两个参数，累积计算
from functools import reduce

reduce(lambda x, y: x + y, [1, 2, 3])  # ((1+2)+3)

# filter(一个函数，一个Iterable)
# filter传入函数返回True/False，只保留列表中True的字段
reduce(lambda x: x % 2 == 0, [1, 2, 3])  # 返回偶数

# sorted(一个Iterable，一个函数，reverse=bool)
# sorted通过函数返回要比较的东西，reverse决定是否要逆置
sorted(['zbc', 'Adk', 'bdd'], key=str.lower, reverse=True)  # ['zbc','bdd','Adk']
```

### 2. <span id = '###32'>返回函数</span>

> 将函数作为返回值返回  
> **返回函数不要引用任何循环变量，或者后续会发生变化的变量**  
> 使用`nonlocal`来引用外部函数的变量

```python
# 定义了一个延迟加载的函数
def lazy_add(x, y):
    def add():
        return x + y

    return add


# t是一个函数
t = lazy_add(1, 2)

# 此时才会执行add()函数
t()       
```

### 3. <span id = '###33'>匿名函数</span>

> 就是`lambda函数`  
> `lambda函数`只能有一个表达式，不用写return，返回值就是该表达式的结果

```python
def build(x, y):
    return lambda: x, y
```

### 4. <span id = '###34'>装饰器</span>

> 在不改变原来函数的基础上，动态增加函数的功能  
> 一个函数上可以使用多个装饰器，调用方式类似递归

```python
import functools


# 在原先sum基础上打印信息
def log(fun):
    # 将fun信息复制到wrapper中，防止未知错误
    @functools.wraps(fun)
    def wrapper(*args, **kw):
        print("call %s():" % fun.__name__)
        return fun(*args, **kw)


@log
def sum(a, b):
    return a + b


# 函数对象__name__可以拿到函数的名字
t = sum
t.__name__  # sum

```

### 5. <span id = '###35'>偏函数</span>

> 给函数设置默认值，简化调用

```python
import functools

int2 = functools.partial(int, base=2)
# 此处int2函数默认设置二进制转换
int2('10001')
# 也可以设置其他的
int2('10001', base=10)
```

## 4. <span id = '##4'>模块</span>

------

> 一个.py文件就是一个模块  
> 一个含有__init__.py就是一个包  
> [第三方库查询网站](https://pypi.org/)  
> 查看已安装的内置模块和第三方模块方法
>
>     import sys
>     sys.path

````python
#!/usr/bin/env python3         #Mac和Linux必须
# -*- coding: utf-8 -*-        #编码环境

' a test module '  # 模块描述

__author__ = 'Wang Gang'  # 作者

if __name__ == '__main__':  # 作为模块内的测试用
    pass
````

## 5. <span id = '##5'>面向对象编程</span>

> 将对象作为基本单元，更加抽象  
> 面向对象三大特点：封装、继承和多态
>
>     私有变量：__name，不可以直接访问，但可以通过实例._类名__name来访问
>             _name，可以直接访问，但不建议直接访问
>     特殊变量：__name__，可以直接访问
>

### 1. <span id = '###51'>类和实例</span>

> 格式：`class` + 类名(继承类)  
> object类为所有类的基类

```python
class Person(object):
    pass


class Student(Person):

    # self 表示创建的实例本身，
    # 对self的操作 = 对实例操作
    def __init__(self, name, score):
        self.__name = name  # 对变量添加__表示私有化，外部无法访问到（一定程度上）
        self.__score = score

    # 封装：将变量封装起来，直接调用，透明
    def to_string(self):
        print("名字是：%s，分数为：%s" % (self.__name, self.__score))


# 创建实例
tom = Student('tom', 98)
```

### 2. <span id = '###52'>访问限制</span>

> 对于禁止外部访问的变量，可以使用`__ + 变量`的形式
> > `private变量`并不是绝对隐秘的，可以通过`实例._类名__变量`的方式引用
>
> > `_ + 变量`的变量原则上来说也不允许访问，但是可以通过实例拿到

```python
class Person(object):

    def __init__(self, name, score):
        # __name 外部无法通过实例调用
        self.__name = name
        self._score = score


tom = Person()

# 以下方式无法获取name属性
tom.__name

# 以下方式可以（强烈不建议）
tom._Person__name

# 可以正常拿到score（不建议）
tom._score
```

### 3. <span id = '###53'>继承和多态</span>

> 对于python来说，不要求严格的传入父类的对象，只要保持方法一致就行：
>
>     class A(object):    class B(A):
>       def run():           def run():
>           print('A')           print('B')
>     
>     class C(object):    # 这里的传参可以是A的子类，也可以不是，只要有run()方法就行
>       def run():        def revoke_run(o):    
>           print('C')        o.run()

```python
class Animal(object):

    def sing(self):
        print("叫声")


class Dog(Animal):

    def sing(self):
        print("汪汪")


class Cat(Animal):

    def sing(self):
        print("喵喵")


def call_sing(animal):
    animal.sing()


cat = Cat()
dog = Dog()

# 不关心传入的是哪个具体类
call_sing(cat)  # 喵喵
call_sing(dog)  # 汪汪

# 多态，动态改变父类的方法，统一接口（符合'开闭'原则）
isinstance(cat, Cat)  # True
isinstance(cat, Animal)  # True
```

### 4. <span id = '###54'>获取对象信息</span>

```python
import types


class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


def fun():
    pass


type(lambda x: x) == types.LambdaType  # True
type(fun) == types.FunctionType
types((x for x in range(3))) == types.GeneratorType
type(abs) == types.BuiltinFunctionType

# 判断类和子类
isinstance()

# 判断含有哪些方法和属性
dir()

obj = MyObject()
hasattr(obj, 'x')  # True
setattr(obj, 'x', 122)  # x = 122
getattr(obj, 'z', 404)  # 获取z的值，没有的话默认为404
hasattr(obj, 'power')  # True
getattr(obj, 'power')()  # 返回方法，并调用
```

### 5. <span id = '###55'>实例属性和类属性</span>

> 实例属性：self.name  
> 类属性：所有实例都可以访问到类属性 **重点：共有共享**
>
>     class Person():
>          name = 'sc'
>
> 避免实例变量和类变量起一样的名字，因为实例变量找不到回去找类变量，引起错误

```python
class Person(object):
    name = 'tom'


obj = Person()

# 由于没有实例变量，所以会找类变量
obj.name  # tom

Person.name  # tom

obj.name = 'jack'
obj.name  # jack

# 类变量赋值
Person.name = 'Lune'

# 删除实例变量
del obj.name
# 由于删除了实例变量，所以会找类变量
obj.name  # Lune


```

## 6. <span id = '##6'>面向对象高级编程</span>

### 1. <span id = '###61'>使用__slots__</span>

> python可以动态赋属性和方法，而`__slots__ = ()`可以限制赋值的属性
>
> 子类不会受到父类设置的`__slots__`影响，除非子类也设置自己的`__slots__`，且设置后会继承父类的

```python
from types import MethodType


class Student():
    __slots__ = ('age', 'score')


def set_score(self, score):
    self.score = score


tom = Student()
jack = Student()
tom.age = 15
tom.age  # 15
jack.age  # 报错，只有tom有age属性
# 给tom 设置方法
tom.set_score = MethodType(set_score, tom)
tom.set_score(68)
tom.score  # 68
jack.set_score(38)  # 报错

# 通过给类设置属性和方法，可以为所有实例共有
Student.set_score = set_score
jack.set_score(58)
jack.score  # 58

# 设置了__slots__，不允许赋值name属性
jack.name = 'jack'  # 报错


class LiHua(Student):
    # 此时，LiHua类可以设置name,age和score属性了
    __slots__ = 'name'
```

### 2. <span id = '###62'>使用@property</span>

> 通过@property可以简化实例变量的的赋值工作  
> **注意：属性的方法名和实例变量不能重名，否则会引起无限调用**

```python
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


d = Person()
# 这里会直接调用set_age()，就像赋值一样，十分方便
d.set_age = 18
d.get_age  # 18
```

### 3. <span id = '###63'>多重继承</span>

> python可以同时继承多个类

```python

class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class EnglishMixIn(object):

    def language(self):
        print("I speak English!")


class Tom(Person, EnglishMixIn):

    def __init__(self, name, age, id):
        super().__init__(name, age)  # 这种方式不需要加self
        # Person.__init__(self,name,age)    这种方式需要加self
        self._id = id

    def to_string(self):
        print("我的名字是：%s，年龄为：%d" % (self.name, self.age))
        EnglishMixIn.language(self)
        # super().language()
```

### 4. <span id = '###64'>定制类</span>

> 介绍一些常用的补充类信息的方法

#### 4.1 <span id = '####641'>\_\_str__、\_\_repr__</span>

```python
class Person(object):

    def __init__(self, name):
        self._name = name

    # 该方法在打印Person('name')时调用
    def __str__(self):
        return 'My name is ', self._name

    # 该方法在打印实例时调用
    def __repr__(self):
        self.__str__()


print(Person('Tom'))  # 调用__str__方法
tom = Person('tom')
print(tom)  # 调用__repr__方法

```

#### 4.2 <span id = '####642'>\_\_iter__、\_\_next__</span>

> 通过实现这两个方法可以使类获得迭代效果

```python
class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    # 获得迭代的变量
    def __iter__(self):
        return self

    # next()方法获取的值
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a


b = Fib()

for n in b:
    print(n)
```

#### 4.3 <span id = '####643'>\_\_getitem__</span>

> 实现上述方法可以让类可以像list一样通过索引获取值，例如：Fib()[5]

```python
class Fib(object):

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


b = Fib()
b[1]  # 1
b[1:3]  # [1,2]
```

#### 4.4 <span id = '####644'>\_\_getattr__</span>

> 当访问一个类中没有的属性时，会报错，可以实现上述方法返回默认值

```python
class Person(object):

    def __getattr__(self, item):
        if item == 'score':  # 返回默认值
            return 98
        elif item == 'age':  # 返回函数
            return lambda x: x + 1


tom = Person()
tom.score  # 98
tom.age(333)  # 334
```

#### 4.5 <span id = '####645'>\_\_call__</span>

> 通过该方法可以直接调用实例对象

```python
class Student(object):

    def __init__(self, name):
        self._name = name

    def __call__(self, *args, **kwargs):
        print("My name is ", self._name)


tom = Student('tom')
tom()  # My name is tom

# 判断变量是否可以调用
callable(tom)  # True
callable([1, 2])  # False
```

### 5. <span id = '###65'>使用枚举类</span>

```python
from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


Weekday.Sun  # Weekday.Sun

Weekday(1)  # Weekday.Mon
```

### 6. <span id  = '###66'>使用元类</span>

> 动态生成类

```python

def fn(self, name):
    print("say", name)


# type(类名，继承父类（元组方式），绑定方法)
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello('Aloha')  # say Aloha
```

## 7. <span id = '##7'>错误、调试和测试</span>

### 1. <span id = '###71'>错误处理</span>

> 当出现错误时，返回错误码的形式固然可以，但是层层上报的话会很啰嗦，
> 可以通过`try...except...finally...`的错误处理机制

> 可以只在需要的地方做错误处理，不必每层都加`try except`

```python
# 格式如下：
try:
    # do some thing
    pass
except ValueError as e:
    # catch error
    pass
except TypeError as e:
    # catch other
    pass

# 如果没有错误，也就是正确执行了try，会走这里
else:
    pass

# 如果设置，则无论正确错误都会走到这里
finally:
    pass
```

#### 1.1 <span id = '####711'>logging、raise</span>

```python
import logging


class ZeroError(ZeroDivisionError):
    pass


try:
    1100 / 0
except ZeroDivisionError as e:
    print('出错了')
    logging.exception(e)
    raise ZeroError('自己包装的zero', e)
```

### 2. <span id = '###72'>调试</span>

> 通过`print()`或`断言`方式  
> 凡是可以通过print调试的，都可以替换为断言
> > 最方便的还是IDE

```python

def foo(n):
    assert n != 0, '%d is zero' % n
    return 10 / n


# assert会断言n!=0，失败则抛出 AssertionError
foo(0)
```

### 3. <span id = '###73'>单元测试</span>

```python
import unittest


class Test(unittest.TestCase):
  
    # 在每次test方法之前调用
    def setUp(self) -> None:
      pass
    
    # 在每次test方法之后调用
    def tearDown(self) -> None:
      pass

    def test_init(self):
        L = [1]
        self.assertTrue(isinstance(L, list))
        self.assertEqual(L[0], 1)
        with self.assertRaises(IndexError):
            L[2]


if __name__ == '__main__':
    unittest.main()  # 运行测试

```