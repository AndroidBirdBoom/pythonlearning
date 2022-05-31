from __future__ import annotations

import urllib.parse
from datetime import datetime, timezone, timedelta
import hashlib, random
import hmac
import itertools
from contextlib import contextmanager

from urllib import request


def demo_time():
    now = datetime.now()
    print(type(now))
    print(now, "时间戳：", t := now.timestamp(), "转换为：", datetime.fromtimestamp(t))
    dt = datetime(2019, 5, 4, 10, 58, 9)
    print(dt, "时间戳：", t := dt.timestamp(), "转换为：", datetime.fromtimestamp(t))
    t = 1546272000000 / 1000
    print("本地时间：", datetime.fromtimestamp(t))
    print("UTC时间：", datetime.utcfromtimestamp(t))
    # str->datetime
    s = '2019-01-01 00:00:00'
    print(t := datetime.strptime(s, '%Y-%m-%d %H:%M:%S'), "时间戳：", t.timestamp(), datetime.fromtimestamp(t.timestamp()))
    print(t := datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "timedata:",
          s := datetime.strptime(t, '%Y-%m-%d %H:%M:%S'), "时间戳：", s.timestamp())

    # 时间计算
    from datetime import timedelta, timezone

    s = '2019-01-01 00:00:00'
    t = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    print(type(t))
    print(t + timedelta(days=10, hours=10))

    # 时区转换
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print("time_zone", utc_dt, type(utc_dt))
    t = datetime.now()
    print(t)
    print(t.replace(tzinfo=timezone.utc))
    print(t.astimezone(timezone(timedelta(hours=10))))

    print(to_timestamp('2015-6-1 08:10:30', 'UTC+7:00'))
    print(to_timestamp('2015-5-31 16:10:30', 'UTC-09:00'))
    print(datetime.fromtimestamp(1433121030).strftime('%Y-%m-%d %H:%M:%S'))


# 2015-1-21 9:01:30 UTC+5:00
import re


def to_timestamp(dt_str, tz_str):
    t = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    print(t)
    p = r'^UTC([+-]\d{1,2}):\d{2}'
    utc = int(re.match(p, tz_str)[1])
    print("utc=>", utc)
    dt = t.replace(tzinfo=timezone(timedelta(hours=utc)))
    return dt.timestamp()


def demo_collection():
    from collections import namedtuple

    Point = namedtuple('Point', ['x', 'y'])
    p = Point(2, 4)
    print(p.x, p.y)
    print(isinstance(p, tuple))

    from collections import deque

    q = deque(['a', 'c', 'd'])
    q.append('e')
    q.appendleft('L')
    print(q)
    q.pop()
    print(q)
    q.popleft()
    print(q)

    from collections import defaultdict

    dd = defaultdict(lambda: 'N/A', {'k1': 'v12', 'k2': 'v2'})
    dd['k1'] = 'v1'
    print(dd.get('k1'))
    print(dd['k1'])
    print(dd['k2'])

    d = dict({'k1': 'v1', 'k2': 'v2'})
    print(d.get('k2'))

    from collections import OrderedDict

    od = OrderedDict()
    od['a'] = 1
    od[1] = 3
    od['2'] = 'fds'
    print(od)
    print(od.popitem(last=True))

    from collections import ChainMap
    import os, argparse

    defaults = {
        'color': 'red',
        'user': 'guest'
    }

    mains = {
        'user': 'ergou'
    }

    cm = ChainMap(mains, defaults)
    print(cm.get('color'))
    print(cm.get('user'))

    from collections import Counter

    c = Counter()
    for ch in 'wanggang':
        c[ch] += 1
    print(c)
    print(c.get('w'))
    c.update('hello')
    print(c)


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def login(user, password):
    if db.get(user):
        return db.get(user) == calc_md5(password)

    return


def demo_hashlib():
    md5 = hashlib.md5()
    md5.update('how to user md5?'.encode('utf-8'))
    print(md5.hexdigest(), len(md5.hexdigest()))
    sha1 = hashlib.sha1()
    sha1.update('how to user sha1?'.encode('utf-8'))
    print(sha1.hexdigest(), len(sha1.hexdigest()))

    print(login('michael', '123456'))
    print(login('bob', 'abc999'))
    print(login('alice', 'alice2008'))

    print(''.join([chr(random.randint(48, 122)) for i in range(20)]))

    print('hello'.encode('utf-8'))
    print(b'hello')

    hm = hmac.new(b'hello world', b'message', digestmod='SHA1')
    print(hm.hexdigest(), len(hm.hexdigest()))

    # natuals = itertools.count(5)
    # for n in natuals:
    #     print(n)


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("error")
        else:
            print('end')

    def query(self):
        print("name is %s" % self.name)


class Querynew(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print("name is %s" % self.name)


@contextmanager
def create_query(name):
    print('begin')
    q = Querynew(name)
    yield q
    print('exit')


urls = 'http://39.105.30.106:8958/api/im/protocol/info?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

url = 'http://www.baidu.com/urllib.parse.html;python?kw=urllib.parse#module-urllib'


def demo_url():
    with create_query('ergou') as f:
        f.query()

    import json

    datas = {'needBody': True, 'type': 1}

    req = request.Request(urls + urllib.parse.urlencode(datas), headers=headers, method='GET')
    with request.urlopen(req) as f:
        data = f.read()
        print(data)
        print(f.getheaders())
        fdata = data.decode('utf-8')
        print(fdata)
        fd = json.loads(fdata)
        print(fd)
        print(fd.get('code'))

    # http://www.baidu.com/urllib.parse.html;python?kw=urllib.parse#module-urllib
    result = urllib.parse.urlparse(url)
    print(result)


from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHtmlParser(HTMLParser):

    def __init__(self):
        super(MyHtmlParser, self).__init__()
        self.collect_data = False
        self.fi_str = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == 'h3' and not self.collect_data:
            for l in attrs:
                if 'event-title' in l:
                    self.collect_data = True
                    self.fi_str = ""

        if tag == 'time' and not self.collect_data:
            for l in attrs:
                if 'datetime' in l:
                    self.collect_data = True
                    self.fi_str = ""

        if tag == 'span' and not self.collect_data:
            for l in attrs:
                if 'event-location' in l:
                    self.collect_data = True
                    self.fi_str = ""

    def handle_endtag(self, tag: str) -> None:
        if tag == 'h3' and self.collect_data:
            self.collect_data = False
            print('会议：', self.fi_str.strip())
            self.fi_str = ""

        if tag == 'time' and self.collect_data:
            self.collect_data = False
            print('时间：', self.fi_str.strip())
            self.fi_str = ""

        if tag == 'span' and self.collect_data:
            self.collect_data = False
            print('地点：', self.fi_str.strip())
            self.fi_str = ""

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        # print('startendtag:', tag)
        pass

    def handle_data(self, data: str) -> None:
        self.fi_str += data

    def handle_comment(self, data: str) -> None:
        # print('comment', data)
        pass

    def handle_entityref(self, name: str) -> None:
        # print('entityref:', name)
        pass

    def handle_charref(self, name: str) -> None:
        # print('charref:', name)
        pass


if __name__ == "__main__":

    import os

    html_file = 'python_events.txt'
    if not os.path.exists(html_file) or not os.path.isfile(html_file):
        with request.urlopen('https://www.python.org/events/python-events/') as r:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(r.read().decode('utf-8'))
    else:
        print('开始分析：=======>')
        with open(html_file, 'r') as f:
            parser = MyHtmlParser()
            parser.feed(f.read())
