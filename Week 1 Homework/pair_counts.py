
# coding: utf-8

# # Problem 5: Pair counts
# 
# This problem consists of a single exercise worth ten (10) points.

# **Exercise 0** (10 points). Given a list of integers, find the number of pairs that are consecutive.
# 
# For example, given the list, `[1, 2, 5, 8]`:
# - the pairs that can be formed from the given list are `(1, 2)`, `(1, 5)`, `(1, 8)`, `(2, 5)`, `(2, 8)`, `(5, 8)`;
# - the only pair that has consecutive integers is `(1, 2)` and hence the value to be returned is one (1).
# 
# If elements in the list are repeated, they should be treated as members of a distinct pair. For instance, if the list were `[1, 1, 1, 2, 2, 5, 8, 8]`, then there are three ways to choose `1` and two ways to choose `2`, or a total of $3\times 2=6$ ways to choose the pair `(1, 2)`, so that the answer would in this case be 6.
# 
# The first test case below tests for the correctness of the solution whereas the second one tests for the efficiency of the solution. That is, it should not take too long for the second case to pass! (To get "full credit," try to find a method that takes less than two (2) seconds on the test input of the second test.)
# 
# > _Application note._ Although this might seem like a toy problem to solve, its application forms the basis of _pattern recognition_. For example, suppose you are trying to discover the buying pattern of products in a supermarket and want to figure out if placing two products next to each other impact each others' sales. (Does placing milk next to cereal drive both their sales upwards? Or if placing Muesli next to Cereal will lead to additional Muesli sales, since people who buy cereal would anyway buy Milk even if it is in the other corner of the store?)
# >
# > In mapping that concrete placement problem into this abstract analysis problem, you can think of the list of numbers as the shelf numbers of products in a receipt, and you are trying to find out the number of cases where the products were in adjacent shelves. 

# In[26]:


import numpy as np
import CPSol as cp


# In[28]:


def count_pairs(L):
    assert type(L)==list
    from collections import Counter
    counts = Counter(L)
    unique_items = sorted(counts.keys())
    unique_pairs = zip(unique_items[1:], unique_items[:-1])
    diff_combos = [counts[b] * counts[a] for b, a in unique_pairs if (b-a) == 1]
    
    return sum(diff_combos)


L1=[1,1,1,2,2,3,4,10]
count_pairs(L1)




# In[25]:


# Test cell: Test_Code1

def test_code1():
    L1=[1,2,3,4,5,6,7,8,9]
    L2=[1,1,1,2,2,3,4,10]
    L3=[1,4,7,9]
    L4=[]
    assert count_pairs(L1)==8, "Test Case L1 failed"
    assert count_pairs(L2)==9, "Test Case L2 failed"
    assert count_pairs(L3)==0, "Test Case L3 failed"
    assert count_pairs(L4)==0, "Test Case L4 failed"
    
    print("\n(Passed!)")
    
test_code1()


# In[27]:


# Test cell: Test_Code2

# This test case will test the efficieny of your solution. If it takes too long (>2 min) to run the code,
# please try improving your method.

import numpy as np
biglist = list(np.random.choice(100, 5000, replace=True))

print("Checking correctness on a large, random list...")
result1 = cp.count_pairs_soln(biglist)
result2 = count_pairs(biglist)
assert result1 == result2
print("(Passed correctness check!)")
    
print("\nChecking speed...")
timing = get_ipython().magic('timeit -o count_pairs(biglist)')
assert timing.average < 2.0
print("(Passed timing check!)")


# **Fin!** You've reached the end of this problem. Don't forget to restart the
# kernel and run the entire notebook from top-to-bottom to make sure you did
# everything correctly. If that is working, try submitting this problem. (Recall
# that you *must* submit and pass the autograder to get credit for your work!)
