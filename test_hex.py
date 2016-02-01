import unittest
from hex_motion import f

class TestCases(unittest.TestCase):

    def test1(self):
        self.assertEqual(f("edeqaaaswwdqqs"), (-2,0))
    def test2(self):
        #print(f("6"))
        self.assertEqual(f("6"), "6")
    def test3(self):
        #print(f("0.99"))
        self.assertEqual(f("0.99"), ".9+.09")
    def test4(self):
        #print(f("24601"))
        self.assertEqual(f("24601"), "20000+4000+600+1")
    def test5(self):
        #print(f("6.283"))
        self.assertEqual(f("6.283"), "6+.2+.08+.003")
    def test6(self):
        f("9000000.0000009")
        self.assertEqual(f("9000000.0000009"), "9000000+.0000009")
        
class TestExpandb(unittest.TestCase):

    def test1(self):
        #print(f("0"))
        self.assertEqual(f1("0"), "0")
    def test2(self):
        #print(f("6"))
        self.assertEqual(f1("6"), "6")
    def test3(self):
        #print(f("0.99"))
        self.assertEqual(f1("0.99"), "0.9+0.09")
    def test4(self):
        #print(f("24601"))
        self.assertEqual(f1("24601"), "20000+4000+600+1")
    def test5(self):
        #print(f("6.283"))
        self.assertEqual(f1("6.283"), "6+0.2+0.08+0.003")
    def test6(self):
        f("9000000.0000009")
        self.assertEqual(f1("9000000.0000009"), "9000000+0.0000009")

if __name__ == '__main__':
    unittest.main()