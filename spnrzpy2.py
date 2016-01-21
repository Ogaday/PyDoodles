import re
a=re.split
c='[aeiou]'
i,j=input()
f,l=a(c,i)[0],a(c,j)[0]
print i.replace(f,l),j.replace(l,f)