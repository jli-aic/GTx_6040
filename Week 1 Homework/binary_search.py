
# coding: utf-8

# # Problem 0
# 
# **Fast searching in ordered collections.** This problem consists of just a single exercise, worth ten (10) points. It is about an elementary principle of computer science algorithm design, which is that one can often do things faster if one exploits structure in the input data.

# Suppose you are given a list of **already sorted** numbers.

# In[1]:


A = [2, 16, 26, 32, 52, 71, 80, 88]

# These are already sorted:
assert A == sorted(A)


# Suppose you now want to know whether a certain value exists in this list. A simple way to do that in Python is as follows.

# In[4]:


def contains(A, x):
    """Returns True only if the value `x` exists in `A`."""
    return x in A

print("A contains 32: {}".format(contains(A, 32)))
print("A contains 7: {}".format(contains(A, 7)))
print("A contains -10: {}".format(contains(A, -10)))


# This method works fine and is reasonably fast on small lists. However, if the list is very large, this method can be wasteful, computationally speaking.
# 
# That's because it does **not** take advantage of the fact that `A` is already ordered. In such a case, it should be easier to determine whether the element exists. (How?)

# **Exercise 0** (3 + 7 == 10 points). Write a function, `ordered_contains(S, x)`, that takes an **already sorted** list, `S`, as input, and determines whether it contains `x`. But there is one more condition: your method **must** be **at least ten times faster** than `contains()` for "large" lists!
# 
# In particular, there are two test codes for this exercise. The first one checks that your procedure does, indeed, return the correct result by comparing its output to `contains()`, which we will assume is correct. Correctness is worth three (3) points of partial credit out of ten (10). The second test cell checks whether your implementation is faster than `contains()` for a relatively large, but ordered, list. If your implementation is slower for smaller lists, that is okay!
# 
# > **Hint.** If you can find a standard Python library routine to help you, by all means, use it!

# In[10]:


def ordered_contains(S, x):
    from bisect import bisect # python built in function to bisect lists
    i = bisect(S, x)
    return i > 0 and S[i-1] == x

# binary search
# https://en.wikipedia.org/wiki/Binary_search_algorithm
THRESHOLD__1 = 128 # An "engineering" constant - use to tune speed
def ordered_contains__1(S, x):
    if len(S) <= THRESHOLD__1:
        return contains(S, x)
    midpoint = int(len(S) / 2)
    if x < S[midpoint]:
        return ordered_contains__1(S[:midpoint], x)
    if x > S[midpoint]:
        return ordered_contains__1(S[midpoint+1:], x)
    return True

# The following method improves on the above. Why is it faster? segmenting lists?
THRESHOLD__2 = 8 # An "engineering" constant - use to tune speed
def ordered_contains__2(S, x, l=0, r=None):
    if r is None: r = len(S)
    if (r-l) <= THRESHOLD__2:
        return contains(S[l:r], x)
    midpoint = int((l+r) / 2)
    if x < S[midpoint]:
        return ordered_contains__2(S, x, l, midpoint)
    if x > S[midpoint]:
        return ordered_contains__2(S, x, midpoint+1, r)
    return True


    
print("A contains 32: {}".format(ordered_contains(A, 32)))
print("A contains 7: {}".format(ordered_contains(A, 7)))
print("A contains -10: {}".format(ordered_contains(A, -10)))
print("\n(Did those results match the earlier example?)")


# In[11]:


# Test cell: `test_is_correct` (1 point)

from random import randint, sample

def gen_list(n, v_max, v_min=0):
    return sample(range(v_min, v_max), n)

def gen_sorted_list(n, v_max, v_min=0):
    return sorted(gen_list(n, v_max, v_min))

def check_case(S, x):
    msg = "`contains(S, {}) == {}` while `ordered_contains(S, {}) == {}`!"
    true_solution = contains(S, x)
    your_solution = ordered_contains(S, x)
    assert your_solution == true_solution, msg.format(true_solution, your_solution)

S = gen_sorted_list(13, 100)
print("Checking your code on this input: S = {}".format(S))

check_case(S, S[0])
check_case(S, S[0]-1)
check_case(S, S[-1])
check_case(S, S[-1]+1)

for x in gen_list(50, 100, -100):
    check_case(S, x)
print("\n(Passed basic correctness checks.)")

print("\nTiming `contains()`...")
x = randint(-100, 100)
get_ipython().magic('timeit contains(S, x)')

print("\nTiming `ordered_contains()`...")
get_ipython().magic('timeit ordered_contains(S, x)')

print("\n(This problem is small, so it's okay if your method is slower.)")
print("\n(Passed!)")


# In[12]:


# Test cell: `test_is_faster` (7 points)

N_MIN = 1000000
N_MAX = 2*N_MIN
R_MAX = max(10*N_MAX, 1000000000)

n = randint(N_MIN, N_MAX)
print("Generating a list of size n={}...".format(n))

S_large = gen_sorted_list(n, R_MAX)

print("Quick correctness check...")
x = randint(-R_MAX, R_MAX)
check_case(S_large, x)
print("\n(Passed.)")

print("\nTiming `contains()`...")
t_baseline = get_ipython().magic('timeit -o contains(S_large, x)')
print("\nTiming `ordered_contains()`...")
t_better = get_ipython().magic('timeit -o ordered_contains(S_large, x)')

speedup = t_baseline.average / t_better.average
assert speedup >= 10, "Your method was only {:.2f}x faster (< 1 means it was slower)!".format(speedup)

print("\n(Passed -- you were {:.1f}x faster!)".format(speedup))


# **Fin!** You've reached the end of this problem. Don't forget to restart the kernel and run the entire notebook from top-to-bottom to make sure you did everything correctly. If that is working, try submitting this problem. (Recall that you *must* submit and pass the autograder to get credit for your work!)
