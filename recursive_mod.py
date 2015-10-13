#What if y is negative!!!

def makemakesafe(x):
    def makesafe(y):
        if y >= x:
            y -= x
            y = makesafe(y)
        else:
            return y
        return y
    return makesafe

if __name__ == "__main__":
    mod6 = makemakesafe(6)

    for i in range(100):
        assert(mod6(i)==i%6)
    assert(mod6(-1)==-1%6)
    print "All done!"