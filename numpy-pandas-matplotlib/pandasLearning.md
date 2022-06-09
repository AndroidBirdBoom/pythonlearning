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
> `loc`方法主要是对标签起作用，`iloc`方法对位置索引起作用

### 1. 创建DataFrame

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
# 可以直接选择
df.site
```

### 2. 遍历

```python
import pandas as pd

mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}
pf = pd.DataFrame(mydataset)
pf.head(1)  # 打印头部第一条
pf.tail(2)  # 打印尾部后两条

# 查看index、columns
pf.index
pf.columns
```

### 3. 选择

```python
import pandas as pd

mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}

pf = pd.DataFrame(mydataset)

# 选择行
pf.loc[0]  # 第一行 Series
pf[0:1]  # 切片，第1行  DataFrame
# 选择列
pf.sites  # columns 的叫做 'sites'的列(pf['sites'])
pf.loc[:, ['sites', 'number']]  # 所有行&这两列

# 按位置选
pf.iloc[3]  # 第4行
pf.iloc[:, 1]  # 所有行&第2列
pf.iloc[1, :]  # 第2行&所有列
pf.iloc[1, 1]  # 第2行&第2列

# 布尔选择
pf[pf > 2]
pf[pf.number.isin([1, 3])]  # 查找columns的'number'列中包含【1，3】的行
```

### 4. csv文件

```python
import pandas as pd

# 读取文件
pf = pd.read_csv('../data/nba.csv')

# 写入文件
people = {'name': ['LiHua', 'WangMing', 'Tao'], 'age': [19, 39, 23], 'sex': ['female', 'female', 'male']}
pf = pd.DataFrame(people)
pf.to_csv('../data/people.csv')
```

### 4. json文件

```python
import pandas as pd

# 读取一般文件
pf = pd.read_json('../data/sites.json')

# 读取嵌套文件

```

### 5. 赋值

```python
import pandas as pd

mydataset = {}
df = pd.DataFrame(mydataset, index=['x', 'y', 'z'])

# 按坐标赋值
df.iloc[0, 1] = 45  # df.iat也可以

# 按标签赋值 
df['name', 'x'] = 'wang'
```

### 6. 缺省值

```python
import pandas as pd

df = pd.DataFrame()

# 显示一个df大小的包含True和False的矩阵
df.isna()
# 丢弃缺省数据
df.dropna(how='any')
# 填充缺省数据
df.fillna(value=49)
```