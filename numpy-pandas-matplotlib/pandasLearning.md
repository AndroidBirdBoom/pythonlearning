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

> ��ά����  
> `pandas.DataFrame( data, index, columns, dtype, copy)`

### 1. ����DataFrame

```python
import pandas as pd

# ͨ��dict��������keyֵ��Ϊcolumns��index���Զ���
mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}
df = pd.DataFrame(mydataset, index=['x', 'y', 'z'])

# ͨ���ֵ䴴������keyֵ��Ϊcolumns��index���Զ���
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)

# ͨ���б����������ͬʱ����columns��index
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
df = pd.DataFrame(data, index=['x', 'y', 'z'], columns=['site', 'age'])

# ȡֵ��ȡcolumns����ȡindex
df['site']['x']
# DataFrameȡһ�У����ص���Series
df.loc['x']
# DataFrameȡ���У����صĻ���DataFrame
df.loc[['x', 'z']]
# ����ֱ��ѡ��
df.site
```

### 2. ����

```python
import pandas as pd

mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}
pf = pd.DataFrame(mydataset)
pf.head(1)  # ��ӡͷ����һ��
pf.tail(2)  # ��ӡβ��������

# �鿴index��columns
pf.index
pf.columns
```

### 3. ѡ��

```python
import pandas as pd

mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}

pf = pd.DataFrame(mydataset)

# ѡ����
pf.loc[0]  # ��һ�� Series
pf[0:1]  # ��Ƭ����1��  DataFrame
# ѡ����
pf.sites  # columns �Ľ��� 'sites'����(pf['sites'])
pf.loc[:, ['sites', 'number']]  # ������&������

# ��λ��ѡ
pf.iloc[3]  # ��4��
pf.iloc[:, 1]  # ������&��2��
pf.iloc[1, :]  # ��2��&������
pf.iloc[1, 1]  # ��2��&��2��

# ����ѡ��
pf[pf > 2]
pf[pf.number.isin([1, 3])]      # ����columns��'number'���а�����1��3������
```