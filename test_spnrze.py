import unittest
from spnrz import f

class Testf1(unittest.TestCase):

    def test1(self):
        self.assertEqual(f("plaster", "man"), ("master", "plan"))

    def test2(self):
        self.assertEqual(f("blushing", "crow"), ("crushing", "blow"))

    def test3(self):
        self.assertEqual(f("litigating", "more"), ("mitigating", "lore"))

    def test4(self):
        self.assertEqual(f("strong", "wrangler"), ("wrong", "strangler"))

    def test5(self):
        self.assertEqual(f("def", "ghi"), ("ghef", "di"))

if __name__ == '__main__':
    unittest.main()