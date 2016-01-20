import unittest
from notes import f, convert

c=1.0005777895

class TestNotes(unittest.TestCase):

    def testA0(self):
        for i, note in enumerate(['A0', "A#0"]):
            self.assertEqual(convert(note), i+1)
    def test_sharps_flats_convert(self):
        sharps= ['C#0','D#0','F#0','G#0','A#0','C#3','D#4','F#5','G#6','A#7']
        flats = ['Db0','Eb0','Gb0','Ab0','Bb0','Db3','Eb4','Gb5','Ab6','Bb7']
        for sharp, flat in zip(sharps,flats):
            self.assertEqual(convert(sharp), convert(flat))
    def test_sharps_flats_htz(self):
        sharps= ['C#0','D#0','F#0','G#0','A#0','C#3','D#4','F#5','G#6','A#7']
        flats = ['Db0','Eb0','Gb0','Ab0','Bb0','Db3','Eb4','Gb5','Ab6','Bb7']
        for sharp, flat in zip(sharps,flats):
            self.assertEqual(f(sharp),f(flat))
            
class TestCases(unittest.TestCase):
    def test1(self):
        assert(27.500/c < f("A0") < 27.500*c)    # 27.500
    def test2(self):
        assert(261.626/c < f('C4') < 261.626*c)
    def test3(self):
        assert(184.997/c < f('F#3') < 184.997*c)
    def test4(self):
        assert(1864.66/c < f('Bb6') < 1864.66*c)
    def test5(self):
        assert(1864.66/c < f('A#6') < 1864.66*c)
    def test6(self):
        assert(440/c < f('A4') < 440*c)
                         
      

if __name__ == '__main__':
    unittest.main()