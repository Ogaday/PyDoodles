import re
def f(*g):a,b=[re.split("[aeiou]",r)[0] for r in g];return b+g[0][len(a):],a+g[1][len(b):]