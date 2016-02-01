# http://codegolf.stackexchange.com/questions/70180/coding-convention-conversion

f = lambda s:(''.join([a.replace(a,'_'+a.lower()) if a.isupper() else a for a in s])[1:],''.join([a[0].upper()+a[1:] for a in s.split('_')]))['_'in s]
import re
f=lambda s:('_'.join(re.findall('[A-Z][a-z]*',s)).lower(),''.join([a[0].upper()+a[1:]for a in s.split('_')]))[s.islower()]

import unittest

class TestCases(unittest.TestCase):

    def test1(self):
        self.assertEqual(f("CodingConventionConversion"), 'coding_convention_conversion')
    def test2(self):
        self.assertEqual(f("coding_convention_conversion"), "CodingConventionConversion")
    def test3(self):
        self.assertEqual(f("Abc"), "abc")
    def test4(self):
        self.assertEqual(f("abc"), "Abc")
    def test5(self):
        self.assertEqual(f("ABC"), "a_b_c")
    def test6(self):
        self.assertEqual(f("a_b_c"), "ABC")
    def test7(self):
        self.assertEqual(f('A'), 'a')
    def test8(self):
        self.assertEqual(f('a'), 'A')

if __name__ == '__main__':
    unittest.main()