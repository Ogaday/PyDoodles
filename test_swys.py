import unittest
from swys import g

class SayWhatYouSee(unittest.TestCase):
    def test0(self):
        self.assertEqual(g(1,0), 1)
    def test1(self):
        self.assertEqual(g(1,1), '11')
    def test2(self):
        self.assertEqual(g(1,2), '21')
    def test3(self):
        self.assertEqual(g(1,3), '1211')
    def test4(self):
        self.assertEqual(g(1,4), '111221')
    def test5(self):
        self.assertEqual(g(11114413311,1),'4124112321')

if __name__ == '__main__':
    unittest.main()