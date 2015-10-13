square = lambda x: x**2
seq = list(range(10))

for m in map(square, seq):
    print(m)
