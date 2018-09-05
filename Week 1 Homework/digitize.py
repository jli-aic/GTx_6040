
# coding: utf-8

# # Problem 9
# 
# This problem consists of a single exercise worth ten (10) points.

# **Exercise 0** (10 points): Write a funtion, `digitize(n)`, that, given a postive number `n`, returns the digits of `n` as the integer elements of a list in reversed order.
# 
# For example:
# 
# ```python
#     assert digitize(1345328) == [8, 2, 3, 5, 4, 3, 1]
# ```

# In[25]:


def digitize(n):
    assert n > 0, '`n` is not a positive number'
    assert type(n) is int, '`n` must be an `int`'
    list_L = list(str(n))
    list_L = list_L[::-1]
    list_L = list(map(int, list_L))
    
    return list_L
        
digitize(1345328)


# In[26]:


# Test_cell: test_digitize

assert digitize(1345328) == [8, 2, 3, 5, 4, 3, 1], 'Wrong output. Make sure your function returns the digits in reverse order'
print("\n(Passed!)")


# **Fin!** You've reached the end of this problem. Don't forget to restart the
# kernel and run the entire notebook from top-to-bottom to make sure you did
# everything correctly. If that is working, try submitting this problem. (Recall
# that you *must* submit and pass the autograder to get credit for your work!)
