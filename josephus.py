a = 10
b = 3

c = []
*d, = range(a)
i = 0

while i < len(d):
    if (i+1)%b == 0:
        c.append(d[i])
    else:
        d.append(d[i])
    i+=1

print(c)
print(d)

def f(a,b):
 c=[];i=0;*d,=range(10)
 while i<len(d):(c,d)[-~i%b>0].append(d[i]);i+=1
 return c

def j(m,n):
    *a,b=*range(m),[]
    while a:a.rotate(-n);b.append(a.pop())
    return b

if __name__=="__main__":
    assert(f(10,3) == [2, 5, 8, 1, 6, 0, 7, 4, 9, 3])