import unittest
class Test1(unittest.TestCase):
    def runTest(self):
        print('test1 is passed')
    def runTest2(self):
        print('test2 is passed')
if __name__ == '__main__':
    unittest.main()
