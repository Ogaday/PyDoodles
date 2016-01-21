i=input()
print type(i)
f=l=''
A='aeiou'
for j in A:
 I=i[0];J=I.find(j)
 if ~J:
  if f:
   if f>I[0][:J]:f=I[:J];break
  else:f=I[:J]
for j in A:
 Y=i[1];J=Y.find(j)
 if ~J:
  if l:
   if l>Y[:J]:l=Y[:J];break
  else:l=Y[:J]
print I.replace(f,l,1),Y.replace(l,f,1)