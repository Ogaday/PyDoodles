import sys
file = sys.argv[1]+'.csv'
content = sys.argv[2]

with open(file, 'w') as f:
    f.write(content)

