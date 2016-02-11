def g(a,b):
 if b<1:return a
 else:
  c,n=1,'';f,*a=str(a)+'_'
  for i in a:
   if i==f:c+=1
   else:n+=str(c)+f;f,c=i,1
  return g(n,b-1)

if __name__=="__main__":
    print(g(11114413311,1))
    print(g(1,3))
    print(g(1,4))