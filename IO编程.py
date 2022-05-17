from io import StringIO
from io import BytesIO


class Demo(object):

    def __enter__(self):
        print("inter")
        return "Demo"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


def demo_io():
    with Demo() as d:
        print("==>", d)

    with open('demo.txt', 'a') as f:
        for i in range(5):
            f.write("行数：%d\n" % i)

    with open('demo.txt', 'r', encoding='gbk', errors='ignore') as f:
        while True:
            r = f.read(3)
            if r == '':
                break
            print(r)

    f = StringIO()
    f.write("Hello")
    f.write(" ")
    f.write("World!")
    print(f.getvalue())

    file = StringIO("Hello\nWorld!\n")
    for line in file.readlines():
        print(line.strip())

    with StringIO("Hi\nHi!\n") as f:
        print(f.getvalue())

    ff1 = BytesIO()
    ff1.write('中文'.encode('utf-8'))
    print(ff1.getvalue().decode('utf-8'))

    ff1.write('hello'.encode('utf-8'))
    print(ff1.getvalue())


import os

from pathlib import Path


def find_file(root_path, name):
    L = []
    for f in os.listdir(root_path):
        if os.path.isdir(f):
            result = find_file(f, name)
            if len(result) > 0:
                L = L + result
        else:
            if name in os.path.split(f)[1]:
                L.append(f)

    return L


def demo_file():
    print(os.name)
    root_project = os.path.abspath('.')
    print(root_project)
    dir_project = os.path.join(root_project, 'demodir')
    dir_path = Path(dir_project)
    print(dir_project)

    f1 = os.path.join(root_project, 'demo.txt')
    f1_path = Path(f1)

    if os.path.isdir(dir_project):
        print("dir is exits!")
    else:
        os.mkdir(dir_project)
    if dir_path.exists():
        print('dir or file is exits!')

    if dir_path.is_dir():
        print("%s is a fir" % os.path.split(dir_project)[1])

    if os.path.isfile(f1):
        print("%s is a file, and prefix is %s" % (os.path.split(f1)[1], os.path.splitext(f1)[1]))

    if dir_path.exists() and dir_path.is_dir():
        # dir_path.rmdir()
        os.rmdir(dir_project)

    if os.path.exists(f1) and os.path.isfile(f1):
        # os.remove(f1)
        print(os.path.split(f1)[0])
        os.rename(f1, os.path.join(os.path.split(f1)[0], 'f2.txt'))

    print(find_file(root_project, '2'))


import pickle
import json
from hello import Hello


def hello2dict(hel):
    return dict(hel=hel.hel)


def dict2hello(d):
    return Hello(d['hel'])


if __name__ == "__main__":
    d = dict(name='wang', age=18)
    t = pickle.dumps(d)
    print(t)
    print(pickle.loads(t))
    with open('f2.txt', 'wb') as f:
        pickle.dump(d, f)

    with open('f2.txt', 'rb') as f:
        d = pickle.load(f)
        print(d)

    # ------------------------------------- json --------------------------------
    dj = json.dumps(d)
    print(dj)
    print(json.loads(dj))

    with open('f2.txt', 'w') as f:
        json.dump(d, f)

    with open('f2.txt', 'r') as f:
        d = json.load(f)
        print(d)

    j = '{"age":18,"person":true,"friends":[{"name":"小刚"},{"name":"梨花"}]}'
    print(json.loads(j))

    h = Hello('yaho')
    hd = json.dumps(h, default=hello2dict)
    print(hd)
    print(json.loads(hd, object_hook=dict2hello))

    with open('f2.txt', 'w') as f:
        json.dump(h, f, default=hello2dict)

    with open('f2.txt', 'r') as f:
        h = json.load(f, object_hook=dict2hello)
        print(h)
