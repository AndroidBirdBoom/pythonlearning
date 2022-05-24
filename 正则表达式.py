import re


def is_valid_email(addr):
    p = r'^[\d\w]+[.]?[\d\w]+@\w+[.]com$'
    if re.match(p, addr):
        return True
    else:
        return False


def name_of_email_1(addr):
    p = r'@'
    t = re.split(p, addr)
    if len(t) > 1:
        s = t[0]
        p1 = r'^<(.+)>(.+)$'
        if t := re.match(p1, s):
            return t.group(1)
        else:
            return s


def name_of_email(addr):
    p = r'<?([A-Za-z\s]+)>?'
    return re.match(p, addr).group(1)


if __name__ == "__main__":
    s = 'ABC\\-010'
    s1 = r'ABC-010'
    s2 = r'\w{3}\-\d{3,5}'
    if re.match(s2, 'ABC-010'):
        print("match")
    else:
        print("not match")

    s = 'a, b,;  c'
    print(s.split(' '))
    p = r'\s+'
    print(re.split(p, s))
    p2 = r'[,\s]+'
    print(re.split(p2, s))
    p3 = r'[,\s,;]+'
    print(re.split(p3, s))

    s = '010-47398'
    if t := re.match(r'^(\d{3})\-(\d{3,8})$', s):
        print(t.group(0))
        print(t.group(1))
        print(t.group(2))
        print(t.groups())
    s = '19:50:39'
    p1 = r'^(0\d|1\d|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
    if t := re.match(p1, s):
        print(t.groups())

    s = '102300rter'
    p = r'^(\d+?)(0*?)([a-z]+)$'
    if t := re.match(p, s):
        print(t.groups())

    re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')

    s = '010-12345'

    if t := re_tel.match(s):
        print(t.groups())

    print(is_valid_email('someone@gmail.com'))
    print(is_valid_email('bill.gates@microsoft.com'))
    print(name_of_email('<Tom Paris> tom@voyager.org'))
    print(name_of_email('bob@example.com'))

    print(re.search(r'com', 'www.baidu.com').span())

    print(re.sub(r'\d+', '@', '121kl402.com', 1))

    phone = "2004-959-559 # 这是一个国外电话号码"
    print(re.sub(r'#.*', '', phone, 0))
    print(re.sub(r'\D+', "", phone, 0))
