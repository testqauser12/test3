import unittest
class Test1(unittest.TestCase):
    def runTest(self):
        print('test1 is passed')
    def runTest2(self):
        print('test2 is passed')
 class Test2(unittest.TestCase):
    def runTest3(self):
        print('test3 is passed')
    def runTest4(self):
        print('test4 is passed')
if __name__ == '__main__':
    unittest.main()
