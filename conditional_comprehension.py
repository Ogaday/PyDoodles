# conditional_comprehension.py
# python 3.5
# Ogaday

# Benchmark for different strategies of list comprehension when inclusion of elements in the list is conditional.
# This a question in the case where inclusion of an element is only desited if the when it is operated on it
# satisfies a condition. This will often cause the element to be operated on twice, which for expensive
# operations, could be detrimental to performance. The alternative, however, looks more kludgy and requires two
# comprehensions, though my instinct is that this will give mor even performance.
#
# We will follow two strategies:
#  1. Two list comprehensions, so that the outer checks whether the elements in the inner satisfy the condition
#  2. A single list comprehension where the element is operated twice. Once for inclusion, then for condition
#     satisfaction.

import timeit

def include(e):
    """A test on element e. Returns true if e is to be included, else false. Other names: test, desirable, satisfies, etc."""
    if e%2 == 0:
        return True

def operate(e):
    """A function of an element e. Return the transformed element."""
    return e

N = 100000
times = [0,0,0]

print("Case 1...")
times[0] = timeit.timeit('[e for e in [operate(e) for e in range(N)] if include(e)]', globals=globals(), number=1000)

print("Case 2...")
times[1] = timeit.timeit('[operate(e) for e in range(N) if include(operate(e))]', globals=globals(), number=1000)

# Note: another idea: do a generator comprehension for the inner comprehension, rather that a list. That is surely
# more efficient, because it mitigates the comprehension of two lists that must be drawing back approach 1.
print("Case 3...")
times[2] = timeit.timeit('[e for e in (operate(e) for e in range(N)) if include(e)]', globals=globals(), number=1000)

for i, time in enumerate(times):
    print("Method " + str(i) + " took " + str(time) + " seconds.")
