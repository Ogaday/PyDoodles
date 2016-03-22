def folder(n, k):
    """
    Generate k folds (boolean masks) over the range n such that no one index is repeated.
    """
    foldsize = n//k
    for i in range(k):
        yield np.array([False if j < i*foldsize or j >= (i+1)*foldsize else True for j in range(n)])
        
def folds(N, k, infold=True):
    """Generate k folds (boolean masks) over the interval [0, N)"""
    s = N//k
    r = N%k
    for i in range(k):
        fold = np.array([not infold if j < i*s or j >= i*s+s else infold for j in range(N)])
        if r and i<r:
            fold[~i] = infold
        yield fold