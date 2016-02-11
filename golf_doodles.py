*k,=map(ord,input())
print([[int(k[i]==x)for i,v in enumerate(k)]for x in range(65,max(k)+1)])

*k,=map(ord,input());print([[int(v==x)for i,v in enumerate(k)]for x in range(65,max(k)+1)])

*k,=map(ord,input());print([[int(v==x)for v in k]for x in range(65,max(k)+1)])
*k,=map(ord,input());print([[int(v==x+65)for v in k]for x in range(26)][:max(k)])

*k,=map(ord,input());print([[(v==x)%for v in k]for x in range(65,max(k)+1)])

*k,=map(ord,input());print([[int(v==x)for v in k]for x in range(65,max(k)+1)])

lambda a,b:`a`+' is '+['equal to ','greater than ','less than '][cmp(a,b)]+`b`
A,B=input();print A,'is',['equal to','greater than','less than'][cmp(A,B)],B

lambda a,b:print(a,'is',[['equal to','greater than'][a>b],'less than'][a<b],b)

lambda a,b:print(a,'is',['equal to','greater than','less than'][(a>b)-(a<b)],b)

def f(a,b):x=a>b;print(a,'is',['equal to','greater than','less than'][x-not x],b)
    
lambda a,b:a.lower()in['2','to','too','two','t0']and b.lower()in['b','be','bee','b3']
lambda a,b:a.lower()in'2 to too two t0'.split()and b.lower()in['b','be','bee','b3']
lambda a,b:a.lower()in'2 to too two t0'.split()+b.lower()in['b','be','bee','b3']>1

lambda x:sum([y.lower()in s.split() for y,s in zip(x,['2 to too two t0','b be bee b3'])])>1

def f(x):s=['2 to too two t0','b be bee b3'];return sum([x[i].lower()in s[i].split() for i range(2)])>1

'2|t(0|oo?|wo)'
'b(ee?|3)?'

import re
lambda a,b:re.sub('2|t(0|oo?|wo)','',a.lower())+re.sub('b(ee?|3)?','',b.lower())==''

from re import*
lambda a,b:sub('2|t(0|oo?|wo)','',a)+sub('b(ee?|3)?','',b)==''

import re
lambda a,b:re.fullmatch('2|t(0|oo?|wo)',a)+re.fullmatch('b(ee?|3)?',b)==''

import re
lambda*x:sum([re.sub(m,'',y.lower()) for y,m in zip(x,['2|t(0|oo?|wo)','b(ee?|3)?'])])>1