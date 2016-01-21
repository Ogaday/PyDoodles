import unittest
from spoonerize import spoonerize

class TestSpoonerize(unittest.TestCase):

    def test1(self):
        self.assertEqual(spoonerize("plaster", "man"), ("master", "plan"))

    def test2(self):
        self.assertEqual(spoonerize("blushing", "crow"), ("crushing", "blow"))

    def test3(self):
        self.assertEqual(spoonerize("litigating", "more"), ("mitigating", "lore"))

    def test4(self):
        self.assertEqual(spoonerize("strong", "wrangler"), ("wrong", "strangler"))

    def test5(self):
        self.assertEqual(spoonerize("def", "ghi"), ("ghef", "di"))

if __name__ == '__main__':
    unittest.main()