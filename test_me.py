# Tests taken from ivory.idyll.org/articles/nose-intro.html
def testOne():
    pass

class TestExampleTwo:
    def testTwoA(self):
        pass

    def testTwoB(self):
        assert False

class TestExampleThree:
    def setUp(self):
        print "Now setting up"
    def tearDown(self):
        print "Now tearing down"
    def testThreeA(self):
        print "I am test Three A"
    def testThreeB(self):
        print "I am test Three A (asserting False)"
        assert False
    def testThreeC(self):
        print "I am test Three A"
