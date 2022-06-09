import pandas as pd
import numpy as np
import json

mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}


def demo_pandas1():
    myvar = pd.DataFrame(mydataset)
    print(myvar)
    print(myvar['sites'][1])

    a = [1, 2, 3]
    myvar = pd.Series(a)
    print(myvar)
    print(myvar[2])

    myvar = pd.Series(mydataset['sites'], index=['x', 'y', 'z'])
    print(myvar)
    print(myvar['y'])

    myvar = pd.Series(mydataset)
    print(myvar)
    print(myvar['number'])

    sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
    myvar = pd.Series(sites, index=[1, 2], name='ERGOU')
    print(myvar)
    try:
        a = 1
        print('fdd')
        raise Exception("ddd")
    except Exception as e:
        print('error', e)

    data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
    df = pd.DataFrame(data, columns=['Site', 'age'], index=['x', 'y', 'z'])
    print(df)
    print(df['age']['x'])
    df = pd.DataFrame(mydataset, index=['x', 'y', 'z'])
    print(df)
    print(df['sites']['z'])

    data = [{'a': 1, 'b': 2}, {'a': 23, 'c': 244}]
    df = pd.DataFrame(data)
    print(df)
    print(df.loc[0], type(df.loc[0]))
    # print(df[0])
    print(df.loc[[0, 1]], type(df.loc[[0, 1]]))
    print(df.loc[0])

    data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
    df = pd.DataFrame(data, index=['x', 'y', 'z'], columns=['site', 'age'])
    print(df)
    print(df.loc[['x', 'z']])


def demo_df():
    s = pd.Series([1, 3, 5, np.nan, 6, 8], index=['x', 'y', 'z', 'm', 'n', 'd'])
    print(s)
    dates = pd.date_range('20130101', periods=6)
    print(dates, type(dates))
    df = pd.DataFrame(np.random.random((6, 4)), index=dates, columns=list('BACD'))
    print(df)
    df2 = pd.DataFrame(
        {'A': 1., 'B': ['20130101', '20130102', '20130103', '20130104'], 'C': pd.Series(1, index=list(range(4))),
         'D': np.array([3] * 4)})
    print(df2)
    print(df.head(2))
    print(df.tail(2))
    print(df2.index, df2.columns)
    print(df.to_numpy())
    print(df)
    print(df.describe())
    print(df.T)
    print(df)
    print(df.sort_index(axis=1, ascending=False))
    print(df.sort_values(by='C'))
    df = pd.DataFrame(mydataset)
    print(df)
    print(df.loc[1])
    print(df['sites'], type(df['sites']))
    print(df.sites)
    print(df)
    print(df[0:2])
    print(df.number)
    print(df[0:1], type(df[0:1]))
    print(df)
    print(df.loc[:, ['sites', 'number']])

    print(df2)
    df2.index = ['a', 'b', 'c', 'd']
    print(df2)
    print(df2.loc['a':'c', ['A', 'C']])
    print(df2[0:2])
    print(df2.loc['a', ['A', 'B']])
    print(df2.loc['a', 'B'])
    print(df2)
    print(df2.iloc[2], type(df2.iloc[2]))
    print(df2.iloc[:, 1])
    print(df2)
    print(df2.iloc[[0, 2], [1, 3]])
    print(df2)
    print(df2[df2.B > '20130103'])
    df3 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list('ABC'), columns=['apple', 'orange', 'banana', 'tan'])
    print(df3)
    print(df3[df3.tan.isin([1, 2, 5, 6, 3, 11])])

    # df4 = df3.copy()
    # print(df4['tan'])

    def demo_csv_json():
        df = pd.read_csv('../data/nba.csv')
        print(df.to_string())
        print('------------')
        print(df.head(10))
        print('------------')
        print(df.tail(5))
        print(df)
        d = {'name': ['LiHua', 'WangMing', 'Tao'], 'age': [19, 39, 23], 'sex': ['female', 'female', 'male']}
        df1 = pd.DataFrame(d)
        print(df1)
        df1.to_csv('../data/people.csv')
        print(df.info())

        URL = 'https://static.runoob.com/download/sites.json'

        df2 = pd.read_json('../data/sites.json', encoding='GB18030')
        print(df2.to_string())

        df3 = pd.read_json(URL)
        print(df3)

        try:
            df4 = pd.read_json('../data/nest_list.json')
            print(df4)
        except Exception as e:
            with open('../data/nested_list.json', 'r') as f:
                data = json.load(f)
                print(data)

            df4_nested = pd.json_normalize(data, record_path=['students'])
            print(df4_nested)

            df5 = pd.json_normalize(data, record_path=['students'], meta=['school_name', 'class'])
            print(df5)

        try:
            df6 = pd.read_json('../data/nested_mix.json')
            print(df6)
        except Exception as e:
            with open('../data/nested_mix.json', 'r') as f:
                data = json.loads(f.read())
                print(data)
            df6_nested = pd.json_normalize(data, record_path=['students'],
                                           meta=['class', 'school_name', ['info', 'president'], ['info', 'address'],
                                                 ['info', 'contacts', 'tel'], ['info', 'contacts', 'email']])

            print(df6_nested.to_string())


if __name__ == "__main__":
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
    print(s1)

    df = pd.DataFrame(
        {'name': ['zhao', 'qian', 'sun', 'li'], 'age': [13, 37, 82, 32], 'sex': ['male', 'female', 'male', 'male']})
    print(df)
    df.age = 39
    print(df)
    df[3:] = ['xie', 22, 'female']
    print(df)
    datas = ['x', 'y', 'z', 'g']
    df.index = datas
    df.at[datas[0], 'age'] = 66
    print(df)
    df.at['y', 'age'] = 9
    print(df)
    df.iloc[0, 2] = 'Null'
    print('\n', df)
    df.iat[0, 2] = 'male'
    print('\n', df)

    df.loc[:, 'age'] = [1, 20, 38, 18]
    print(df)
    df2 = df.reindex(index=datas, columns=list(df.columns) + ['adr'])
    print(df2)
    df2.loc['x':'z', 'adr'] = ['sd', 'jn', 'dd']
    print(df2)
    df2.iloc[0:2, 3:] = ['xx', 'xx']
    print(df2)
    df2.loc['x', 'age'] = 28
    print('\n', df2)
    print(df2.loc[:, ['adr', 'age']])
    print(df2)
    print(df2.dropna(how='any'))
    print('\n', df2.fillna(value='zz'))
    print(df2.isna())
    print(df2, '\n')
    df2.loc['x', 'age'] = np.nan
    print(df2, '\n')

    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df, '\n')
    print(df.mean(), '\n')
    print(df.mean(1), '\n')

    s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
    print(s)
    print(df.sub(s, axis='index'))

