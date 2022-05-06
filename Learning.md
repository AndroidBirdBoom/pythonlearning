## 函数

----------

### 1. 格式：

```python
def function_name(a, b):
    # 如果不加return，默认返回None.
    return 
```

### 2. 返回多个值

> **python中的函数可以返回多个值**，简单来说就是返回了一个元组（tuple）

### 3. 函数参数

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

#### 1. 可变参数

> 当调用的函数参数不明确时，可以使用可变参数
> 1. 可变参数传入在函数中组装为一个tuple

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

#### 2. 关键字参数

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

## 高级特性

-----

### 1. 切片

> 可以对list或tuple进行切片操作，一次性截取多个元素
> 1. 也可以对str进行切片

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

### 2. 迭代

> 可以理解为数组的遍历，但是python中不止可以遍历list/tuple，还可以遍历dict。事实上，**<font color="red">只要是可迭代对象，都可以使用for in 遍历</font>**
> 1. str也可以迭代

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

### 3. 列表生成器

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
L = [x if x == 3 else x//2 for x in range(1, 11) if x % 3 == 0] 
```

### 4. 生成器
> 没太明白使用场景

### 5. 迭代器
