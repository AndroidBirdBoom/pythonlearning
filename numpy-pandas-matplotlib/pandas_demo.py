import pandas as pd

mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3]
}
if __name__ == "__main__":
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
