from random import*
m='rps'
c=choice(m)
print(c,'twl'[m.find(input())-m.find(c)])

from random import*
m='rps'
c=choice(m)
print(c,(m.find(input())-m.find(c))%3)

from random import*
m='rps'
c=randint(0,2)
print(m[c],(m.find(input())-c)%3)

from random import*
c=randint(0,2)
print('rps'[c],('rps'.find(input())-c)%3)