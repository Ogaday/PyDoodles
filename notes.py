z='C@D@EF@G@A@B'
#def f(n):a,*b,c=n;return int(c),z.index(a)+((-1,1)[b==['#']],0)[not b]
#def f(n):*a,b=n;d=(0,1)[a[-1]=='#'];(d,-1)[a[-1]=='#'];return int(b),z.index(a[0])+d
def f(n):a,*b,c=n;return 2**((int(c)*12+z.index(a)-((9,7)[b==['#']],8)[not b]-49)/12)*440
#2**((-48)/12)*440
def f(n):a,*b,c=n;return 2**(int(c)+('C@D@EF@G@A@B'.find(a)-((22,20)[b==['#']],21)[not b])/12)*55    # 97 bytes
#f=lambda n:2**(int(n[-1])+('C@D@EF@G@A@B'.find(n[0])-((22,20)[n[1:-1]=='#'],21)[not n[1:-1]])/12)*55

def convert(n):a,*b,c=n;return int(c)*12+z.index(a)-((9,7)[b==['#']],8)[not b]

if __name__=="__main__":
 
 print('A0',f('A0'))
 print('A#0',f('A#0'))
 print('B0', f('B0'))
 print('C1', f('C1'))
 print('C#1',f('C#1'))
 print('B4',f('B4'))
 print('Db7',f('Db7'))