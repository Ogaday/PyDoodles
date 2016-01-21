#import re
#def spoonerize(word1, word2):
#    vowels = "[aeiou]"
#    a, b = re.split(vowels, word1)[0], re.split(vowels, word2)[0]
#    return b+word1[len(a):], a+word2[len(b):]

#from re import split as s;v="[aeiou]";f=lambda *a: (s(v,a[1])[0]

from re import split as s
def f1(x,y):v="[aeiou]";a,b=s(v,x)[0],s(v,y)[0];return b+x[len(a):],a+y[len(b):]    #106 bytes

from re import split as s
v="[aeiou]";
f2=lambda x,y:(s(v,y)[0]+x[len(s(v,x)[0]):],s(v,x)[0]+y[len(s(v,y)[0]):])    #112 bytes

import re
def f3(x,y):v="[aeiou]";a,b=re.split(v,x)[0],re.split(v,y)[0];return b+x[len(a):],a+y[len(b):]    #104 bytes

re.split=s
def f6(x,y):v="[aeiou]";a,b=s(v,x)[0],s(v,y)[0];return b+x[len(a):],a+y[len(b):]    #100 bytes

def f4(*g):a,b=[re.split("[aeiou]",r)[0] for r in g];x,y=g;return b+x[len(a):],a+y[len(b):]

def f5(*g):a,b=[re.split("[aeiou]",r)[0] for r in g];return b+g[0][len(a):],a+g[1][len(b):]    #10 bytes plus import

def f7(*g):a,b=map(re.split,["[aeiou]"]*2,g);a,b=a[0],b[0];return b+g[0][len(a):],a+g[1][len(b):]    #107 bytes

z=lambda*x:re.split(*x)[0]
def f8(*g):a,b=map(z,["[aeiou]"]*2,g);return b+g[0][len(a):],a+g[1][len(b):]
#return b+g[0][len(a):],a+g[1][len(b):]

def f9(*g):a,b=map(re.split,["[aeiou]"]*2,g);a,b=a[0],b[0];return g[0].replace(a,b,1),g[1].replace(b,a,1)

def f10(*g):a=[re.split("[aeiou]",r)[0] for r in g];return map(str.replace,g,a,a[::-1],[1,1])

#p=lambda a,b,c;a+b[len(c):]

#;return [l[]+g[i][len(m):] for i in [0,1]]

# l[1]+g[0][len(l[0]):],l[0]+g[1][len(l[1]):]

if __name__ == "__main__":
 import sys
 g=sys.argv[1:]
 a,b=[re.split("[aeiou]",r)[0] for r in g]
 print(b+g[0][len(a):],a+g[1][len(b):])
    