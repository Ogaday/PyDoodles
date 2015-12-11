# Python 3.4
# http://stackoverflow.com/questions/34199743/codingbatwarmup-last2-showing-compile-error-on-the-online-compiler-even-though/34200957


def last2a(str):
    match = str[-2:]
    count = 0
    for i in range(len(str)-2):
        if str[i:i+2]==match:
            count+=1
    return count
    
def last2b(string):
    s = string[-2:]
    return sum(string[i:i+2] == s for i in range(len(string))) - bool(s)

def last2c(str):
    s = str[-2:]
    return sum(str[i:i+2] == s for i in range(len(str)-2))

if __name__=="__main__":
    import timeit
    # Many matches
    print(timeit.timeit("last2a('aaaaaaaaaaa')", setup="from __main__ import last2a"))
    print(timeit.timeit("last2b('aaaaaaaaaaa')", setup="from __main__ import last2b"))
    print(timeit.timeit("last2c('aaaaaaaaaaa')", setup="from __main__ import last2c"))
    
    # 0 length string
    print(timeit.timeit("last2a('')", setup="from __main__ import last2a"))
    print(timeit.timeit("last2b('')", setup="from __main__ import last2b"))
    print(timeit.timeit("last2c('')", setup="from __main__ import last2c"))

    # No matches
    print(timeit.timeit("last2a('abcdefghijk')", setup="from __main__ import last2a"))
    print(timeit.timeit("last2b('abcdefghijk')", setup="from __main__ import last2b"))
    print(timeit.timeit("last2c('abcdefghijk')", setup="from __main__ import last2c"))