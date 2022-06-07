## Series

> `pandas.Series( data, index, dtype, name, copy)`

```python
import pandas as pd

mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}

myvar = pd.Series(mydataset['sites'], index=['x', 'y', 'z'], name='ERGOU')
myvar['x']  # Google

myvar = pd.Series(mydataset['sites'], index=[1, 2])
myvar[3]  # KeyError

myvar = pd.Series(mydataset)
myvar['sites'][2]  # Wiki
```

## DataFrame

> 二维数组  
> `pandas.DataFrame( data, index, columns, dtype, copy)`

```python
import pandas as pd

# 通过dict创建，则key值作为columns，index可以定义
mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}
df = pd.DataFrame(mydataset, index=['x', 'y', 'z'])

# 通过字典创建，则key值作为columns，index可以定义
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)

# 通过列表创建，则可以同时设置columns和index
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
df = pd.DataFrame(data, index=['x', 'y', 'z'], columns=['site', 'age'])

# 取值先取columns，再取index
df['site']['x']
# DataFrame取一行，返回的是Series
df.loc['x']
# DataFrame取多行，返回的还是DataFrame
df.loc[['x', 'z']]
```