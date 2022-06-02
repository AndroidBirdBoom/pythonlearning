## Numpy 对象

----

### 1. 基本知识

> `np.array(object,dtype,copy,order,subok,ndmin)`
>
> `dtype`：设置numpy的数据类型(bool_,int_...._)  
> `ndmin`：维度  
> `itemsize`：每个项占用的字节数
> `shape`：几乘几的数组  
> `size`：数组的数据量  
> `nbytes`：所有数据消耗的字节数

```python
import numpy as np

a = np.array(object=[1, 2, 3])
a = np.array([[1, 2, 3], [4, 5, 6]])

a[1, 2] == a[1][2]  # True
```

### 2. 创建数组

```python
import numpy as np

# 全零
a = np.zeros((2, 3))

# 全一
b = np.ones((2, 2))

# 任意值，此例中是全7
c = np.full((2, 3), 7)

# 对角矩阵3*3
d = np.eye(3)

# 随机数据
e = np.random.random((3, 4))
```

### 3. 数组索引

> 切片方式获得的子数组，是原数组的一部分，**改变该数组也会导致原数组的变化**  
> 数组方式不会发生这种问题

```python
import numpy as np

a = np.arange(1, 13).reshape((3, 4))

# 通过切片
b = a[:, 1:3]
b[1, 1] = 100  # 原数组也会发生变化

# 通过整数数组
a = np.array([[1, 2], [3, 4], [5, 6]])
# 获取第0,1,2行的第0,1,0个元素的值
a[[0, 1, 2], [0, 1, 0]]  # [1,4,6]
# 获取第0行0列的元素
a[0, 0]  # 1

# 布尔数组索引
a = np.array([[1, 2], [3, 4]])
b = a > 2  # [[False,False],[True,True]]
a[b]  # [3,4]，返回的都是True的元素

```