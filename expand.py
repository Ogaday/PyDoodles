# http://codegolf.stackexchange.com/questions/68939/expand-the-number
 
def f(n):
 if not eval(n):return "0"
 x=n.split('.');a,b=(x+[''],x)[len(x)-1];p='+.';p=(p,'.')[a=='0'];p=(p,'')[b==''];e=enumerate;return "+".join([d+'0'*i for i,d in e(a[::-1]) if eval(d)][::-1])+p+"+.".join(['0'*i+d for i,d in e(b) if eval(d)])
 


#          [d+'0'*i for i,d in enumerate(a[::-1]) if eval(d)][::-1]
#          [d+'0'*i for i,d in zip(range(0,len(a),-1),a) if eval(d)]
#l=len
e=lambda s:[d+'0'*(len(s)-i-1) for i,d in enumerate(s) if eval(d)]
def f(n):x=n.split('.');a,b=(x+[''],x)[len(x)-1];return['0',"+".join(e(a)+['.'+d[::-1]for d in e(b[::-1])][::-1])][bool(eval(n))]
                          
#def f(n):x=n.split('.');b=('',x[1])[len(x)-1];return['0',"+".join(e(x[0])+['.'+d[::-1]for d in e(b[::-1])][::-1])][bool(eval(n))]                        
#def f(n):x=n.split('.');try:b=x[1]except:b='';return ['0',"+".join(e(x[0])+['.'+d[::-1] for d in e(b[::-1])][::-1])][bool(eval(n))]

def f(n):
 if not eval(n):return "0"
 x=n.split('.');a,b=(x+[''],x)[len(x)-1];e=enumerate;return"+".join([d+'0'*i for i,d in e(a[::-1]) if eval(d)][::-1]+['.'+'0'*i+d for i,d in e(b) if eval(d)])

def f(n):x=n.split('.');a,b=(x+[''],x)[len(x)-1];e=enumerate;return('0',"+".join([d+'0'*i for i,d in e(a[::-1]) if eval(d)][::-1]+['.'+'0'*i+d for i,d in e(b) if eval(d)]))[bool(eval(n))]

def f(n):x=n.split('.');a,b=(x+[''],x)[len(x)-1];e=enumerate;return('0',"+".join([d+'0'*i for i,d in e(a[::-1])if d!='0'][::-1]+['.'+'0'*i+d for i,d in e(b)if d!='0']))[eval(n)!=0]
#                                            bool(eval(n))
#def f(n):x=n.split('.');a,b=(x+[''],x)[len(x)-1];e=enumerate;return('0',"+".join([d+'0'*i for i,d in e(a[::-1]) if d!='0'][::-1]+['.'+'0'*i+d for i,d in e(b) if d!='0']))[n!='0']

#enumerateenumerate
#e=enumerateee;    

# 164 bytes.
def f1(n):
 *m,=n
 try:p=m.index('.');m.pop(p)
 except:p=len(m)
 #if'.'in n:p=m.index('.');m.pop(p)
 #else:p=len(m)
 return('0','+'.join([str(eval(d)*10**(p-i-1))for i,d in enumerate(m)if d!='0']))[eval(n)!=0] 

#;m.pop(p)
#[:p]+m[p:]
#m,o=list(n),'0'
#*m,=n; o='0'

# 189 bytes
def f2(n):
 *m,=n;o='0'
 try:p=m.index('.');m.pop(p)
 except:p=len(m)
#return(o,'+'.join([d+o*(p-i-1) if (p-i)>0 else '0.'+o*(-1*(p-i))+d for i,d in enumerate(m) if d!=o]))[eval(n)!=0]
 return(o,'+'.join([['.'+o*(-1*(p-i))+d,d+o*(p-i-1)][p-i>0]for i,d in enumerate(m)if d!=o]))[eval(n)!=0]
#return(o,'+'.join([d+o*u if u>0 else '0.'+o*u+d for u,d in [p-i,m[i] for i in range(len(m))] if d!=o]))[eval(n)!=0]
#f=lambda n:'+'.join([str(eval(d)*10**(i + n.index('.'))) for i,d in enumerate(list(n).pop(n.index('.')))])
"""
import sys
if __name__=="__main__" and sys.version_info[0]<3:
    i=input().split(".")
    I,e=i[0],enumerate
    o=[(k+len(I[j+1::])*"0") for j,k in e(I) if k!="0"] 
    try:J=i[1];o+=["."+l*"0"+m for l,m in e(J) if m!="0"]
    except:''
    print("+".join(o if o else "0"))
"""