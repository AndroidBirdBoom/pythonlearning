import unittest
from 错误调试和测试 import Dict


class TestDict(unittest.TestCase):

    def setUp(self) -> None:
        print('setUp')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.get('a'), 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
        self.assertTrue('key' in d)

    def test_error(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def tearDown(self) -> None:
        print('tearDown')


if __name__ == '__main__':
    unittest.main()
