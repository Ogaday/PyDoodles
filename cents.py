#a=input()
#a=int(a.replace('.',''))
a=int(float(input())*100)
q = a//25
d = (a-q*25)//10
n = (a-q*25-d*10)//5
p = a%5
print(q,d,n,p)
print(4*'%s '%(q,d,n,p))
print(4*'%s '%(q or'',d or'',n or'',p or''))
c = [q,d,n,p]
e=[' quarter',' dime',' nickel',' penny']
print(' '.join([str(b)+d for b,d in zip([a//25,a%25//10,a%25%10//5,a%5],[' quarter',' dime',' nickel',' penny']) if 0<b]))


assert(25*q+10*d+5*n+p == a)

def f(a):
 a*=100;return' '.join([str(b)+d for b,d in zip([a//25,a%25//10,a%25%10//5,a%5],[' quarter',' dime',' nickel',' penny']) if 0<b])

def f(a):
 for c in'quarter','dime','nickel','penny':
  