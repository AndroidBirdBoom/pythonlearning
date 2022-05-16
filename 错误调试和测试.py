import logging

logging.basicConfig(level=logging.INFO)


def foo(s):
    r = int(s)
    if r == 0:
        raise FooError('invalid value:', r)
    return fun(r)


def fun(r):
    assert r > 0, '%d is less than zero!' % r
    return 10 / r


class FooError(ValueError):
    pass


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == "__main__":

    try:
        print('foo(%s):%s' % ('1', foo('1')))
    except Exception as e:
        logging.exception(e)

    try:
        r = 10 / 2
        print("10 / 2 = ", r)

    except ZeroDivisionError as e:
        print('except:', e)
    except ValueError as e:
        print('value error:', e)
    except TypeError as e:
        print('type error:', e)
    else:
        print('no error')
    finally:
        print('finally')
    print('END')

    foo('10')




