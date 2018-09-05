
# coding: utf-8

# # Problem 1
# 
# This problem has 2 exercises, worth a total of 10 points.

# **Exercise 0** (2 points).  Write a function, `transform` that takes a string and performs the following operations to it: converts the string to lower case letters only and removes any spaces in the string.
# 
# > In this problem, "space" means only the space character, not other forms of whitespace, such as tabs and newlines.
# 
# For example:
# 
# ```python
#   assert transform('Hello, World!') == 'hello,world'
# ```

# In[2]:


def transform(k):
    return k.lower().replace(" ", "")

print(transform('Hello, World!'))


# In[3]:


# Test cell: test_transform

assert transform('HELLO').isupper() is False
assert transform(' ').isspace() is False
assert transform('HeL lO\ttHe\nRe') == 'hello\tthe\nre'

print("\n(Passed!)")


# **Exercise 1** (3 + 5 == 8 points).  Write a function, `remove_dups(S)` that takes a list `S` and removes multiple occurrences of any element. The function returns a list with only one occurrence of each element.
# 
# For example, `remove_dups(['cat', 'dog', 'sheep', 'dog'])` would return `['cat', 'dog', 'sheep']`.
# 
# This exercise has two test cells. The first checks that your implementation returns the right answer. The second tests your solution on a large list. To get full credit, your implementation must take less than a certain amount of time!

# In[4]:


def remove_dups(S):
    return list(set(S))


# In[6]:


# Test cell: test_remove_dups_correct
listA = ['cat', 'dog', 'sheep', 'dog']
listB = [1,2,3,4,3,2,1,5]

assert isinstance(remove_dups(listA), list)

your_listA = remove_dups(listA)
assert len(remove_dups(listA)) == 3 and set(your_listA) == {'cat', 'dog', 'sheep'}
your_listB = remove_dups(listB)
assert len(remove_dups(listB)) == 5 and set(your_listB) == set(range(1,6))

print("\n(Passed!)")


# In[7]:


# Test cell: test_remove_dups_fast

from random import sample
large_list = sample(range(1000000000), 10000)
timing = get_ipython().magic('timeit -o remove_dups(large_list)')
assert timing.average < 1e-2 # 10 ms time limit for 10,000 elements


# **Fin!** You've reached the end of this problem. Don't forget to restart the
# kernel and run the entire notebook from top-to-bottom to make sure you did
# everything correctly. If that is working, try submitting this problem. (Recall
# that you *must* submit and pass the autograder to get credit for your work!)
