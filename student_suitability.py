import numpy as np

np.random.seed(0)

n_subs = 8
students = np.random.randint(0, 100, (800, n_subs+1))
students[:,0] = range(800)
# print(students[:10])

def rank(students, course_weights):
    grades = students[:,1:]
    ids = students[:,0]
    scores = grades@course_weights
    print(scores.shape)

    I = scores.argsort()[::-1]
    return ids[I]

def argrank(students, course_weights):
    grades = students[:,1:]
    ids = students[:,0]
    scores = grades@course_weights
    print(scores.shape)

    I = scores.argsort()
    return I[::-1]

course_weights = [1,0,0,0,0,0,0,0]
print(rank(students, course_weights))


# print(students[rank(students, course_weights), :])
