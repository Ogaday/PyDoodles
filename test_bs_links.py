import unittest

from bs_links import find_lchevs, find_rchev, chevs


class TestFuncs(unittest.TestCase):
    def setUp(self):
        self.test_text = "<This is some text <With nested> <Brackets>> <There are also brackets> <Which <Are <Not<Nested>>>>"
        self.lchevs = [0, 19, 33, 45, 71, 78, 83, 87]
        self.rchevs = [31, 42, 43, 69, 94, 95, 96, 97]
        for c in [self.test_text[i-3:i+3] for i in self.rchevs]:
            print(c)
        for chev in self.lchevs:
            assert(self.test_text[chev] == '<')
        for chev in self.rchevs:
            assert(self.test_text[chev] == '>')

    #def test_find_lchevs(self):
    #    self.assertEqual(list(find_lchevs(self.test_text)), self.lchevs)
    
    #def test_find_rchev(self):
    #    rchevs = []
    #    for i in self.lchevs:
    #        rchevs.append(i+find_rchev(self.test_text[i:]))
    #    self.assertEqual(rchevs, self.rchevs)
    
    #def test_chevs_generator(self):
    #    print(list(chevs(self.test_text)))
    #    self.assertEqual(list(chevs(self.test_text)), list(zip(self.lchevs, self.rchevs)))
    def test_chevs(self):
        print(chevs(self.test_text))
        self.assertEqual(chevs(self.test_text), (self.lchevs, self.rchevs))
if __name__ == '__main__':
    unittest.main()