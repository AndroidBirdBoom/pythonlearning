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
    print("sum = ",s)
    
    
calc(1,3,4)

#也可以使用 * + list 传入list或者tuple
list = [1,3,4,5]
calc(*list)

calc(1,3,4,5,city="北京",age=18)
```

#### 2. 关键字参数
> 1. 关键字参数视为dict
> 2. 命名关键字参数必须传入参数名，否则会调用出错
```python
def person(name,age,**center):
    #查看center中的元素
    if 'city' in center:
        print("city = ",center.get('city')) 

        
#命名关键字通过以下方式：
def person(name,age,*,code,city):
    pass

#如果含有可变参数的话，后面的关键字可以不带*
def person(name,age,*args,city,code):
    pass

#同样的，也可以掺杂默认参数使用
def person(name,age,*,city="北京",code):
    pass

person("hahah")
```
