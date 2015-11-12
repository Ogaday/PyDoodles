import itertools

X = ["a","b"]
Y = ["c","d","e"]
Z= ["f","g"]

for A in itertools.combinations(X,1):
    for B in itertools.combinations(Y,2):
        for C in itertools.combinations(Z, 2):

             print(A, B, C)
