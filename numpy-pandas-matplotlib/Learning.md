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

### 4. 数据类型

> 通过`numpy.array(dtype=)`设置  
> 通过`np.dtype`获取具体类型

### 5. 数组中的数学

```python
import numpy as np

x = np.array([1, 2])
y = np.array([3, 4])
x + y  # == np.add(x,y)
x - y  # == np.subtract(x,y)
x * y  # == np.multiply(x,y)
x / y  # == np.divide(x,y)
x.dot(y)  # == np.dot(x,y)

# 转置T
x.T
```

### 6. 广播

> 广播需要一定的触发机制以及广播规则。  
> 总的来说就是先铺满一面（无论是x,y,z），然后再将一面扩展到其他维度。

```python
import numpy as np

a = np.arange(8).reshape(2, 2, 2)
b = np.arange(2).reshape(1, 2, 1)
# 可以将a想象成一个2*2*2的立方体，那么b就是一个1*2*1的一个长方体。
# 只需要先将b沿x轴扩展为（2,2,1），再沿z轴扩展为（2,2,2）即可！
a + b  # (2,2,2)  

a = np.ones((2, 2, 3))
b = np.ones((2, 3))
# 先将b转置为（1,2,3），再沿x轴扩展为（2,2,3）
a + b  # (2,2,3)

a = np.ones((1, 4, 3))
b = np.ones((4, 1, 5))
a + b  # 报错
```

## 