# http://codegolf.stackexchange.com/questions/70017/motion-on-a-hexagonal-grid
# http://www.redblobgames.com/grids/hexagons/#coordinates

#import re
def transform(c,s):
    #s=['r'*5 if a='R' else a for a in s]
    #re.sub('R',5*'r',s)
    s=s.replace('R',5*'r',s)
    if s:
        # transform
        c = transform(c,s[1:])
    return c

"""
X=[-1,0,1,1,0,-1,0]
Y=[-.5,-1,-.5,.5,1,.5,0]
f=lambda s,x=0,y=0,l='qwedsa': f(s.replace('R',5*'r')[1:],x+X[l.find(s[0])],y+Y[l.find(s[0])],l[-1]+l[:-1] if s[0]=='r' else l) if s else (floor(x),floor(y))
"""
X=[-1,0,1,1,0,-1,0]
Y=[-.5,-1,-.5,.5,1,.5,0]
f=lambda s,x=0,y=0,l='qwedsa': f(s.replace('R',5*'r')[1:],x+X[l.find(s[0])],y+Y[l.find(s[0])],l[-1]+l[:-1] if s[0]=='r' else l) if s else (floor(x),floor(y))


"""
def f(s,x=0,y=0,l='qwedsa'):
    s = s.replace('R',5*'r')
    x=x+X[l.find(s[0])]
    y=y+Y[l.find(s[0])]
    l[-1]+l[:-1] if s[0]=='r' else l
"""    
#(c[0]+d[ ],c[1]+d[ ])
#map(lambda x,y:x+y,a,b)
#[x+y for x,y in zip(a,b)]
#from operator import add; map(add,a,b)