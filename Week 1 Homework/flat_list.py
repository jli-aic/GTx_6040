
# coding: utf-8

# # Problem 4
# 
# This problem consists of a single exercise worth ten (10) points.
# 
# **Exercise 0** (10 points). Complete the function `flatten(L)`, which takes a "complex list," `L`, as input and returns a "flat" copy.
# 
# By complex, we mean that the input list `L` consists of **arbitrarily nested lists of strings and integers**. For instance, here is a complex list:
# 
# ```python
#     L = [['a', ['cat'], 2],[[[3]], 'dog'], 4, 5]
# ```
# 
# Observe that there are strings and integers, but that these may be embedded within lists inside lists inside lists...
# 
# Given such a list, your computational task is to extract all the strings and integers, and return them in a single flattened list. For example:
# 
# ```python
#   assert flatten(L) == ['a', 'cat', 2, 3, 'dog', 4, 5]
# ```
# 
# In your flattened version, the strings and integers must appear in the same "left-to-right" order as they do in the original list. For instance, if you strip out all the square brackets in the definition of `L` above, then observe that `'cat'` appears to the right of `'a'`, and `2` appears to the right of `'cat'`, and `3` appears to the right of `2`, etc.
# 
# > Hint: One reasonable approach to this problem is to use _recursion_, that is, the idea of a function that calls itself to solve subproblems. See "Recursive programs" at the Wikipedia page on [Recursion as it is used in computer science](https://en.wikipedia.org/wiki/Recursion_%28computer_science%29#Recursive_programs).

# In[21]:


def flatten(L):
    assert type(L) is list
    flatL = []
    for i in L:
        if type(i) is not list:
            flatL += [i]
        else:
            flatL += flatten(i)
    
    return flatL



# In[15]:


# Test cell: test_flatten (10 points)

L = [['a',['cat'],2],[[[3]],'dog'],4,5]
FL = flatten(L)
True_L = ['a', 'cat', 2, 3, 'dog', 4, 5]
print("Your result: \n{}".format(FL))
print('True result: \n{}'.format(True_L))
assert type(FL) is list and FL == ['a', 'cat', 2, 3, 'dog', 4, 5]
print("\n")

L = [[1,[['b'],2],'t',[[3]],'snow'],'x',['hat',7]]
FL = flatten(L)
True_L = [1, 'b', 2, 't', 3, 'snow', 'x', 'hat', 7]
print("Your result: \n{}".format(FL))
print('True result: \n{}'.format(True_L))
assert type(FL) is list and FL == [1, 'b', 2, 't', 3, 'snow', 'x', 'hat', 7]
print("\n")

L = ['x',1,'z']
FL = flatten(L)
True_L = ['x',1,'z']
print("Your result: \n{}".format(FL))
print('True result: \n{}'.format(True_L))
assert type(FL) is list and FL == ['x',1,'z']
print("\n")

L = []
FL = flatten(L)
True_L = []
print("Your result: \n{}".format(FL))
print('True result: \n{}'.format(True_L))
assert type(FL) is list and FL == []

print("\n(Passed!)")


# **Fin!** You've reached the end of this problem. Don't forget to restart the kernel and run the entire notebook from top-to-bottom to make sure you did everything correctly. If that is working, try submitting this problem. (Recall that you *must* submit and pass the autograder to get credit for your work!)
