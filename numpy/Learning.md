## Numpy 对象


----
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
```