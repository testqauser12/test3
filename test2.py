import unittest

class Test1(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print('1 test')

class Test2(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print('2 test')

if __name__ == '__main__':
    unittest.main()
