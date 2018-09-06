
# coding: utf-8

# # Problem 3
# 
# This problem has a single exercise worth a total of ten (10) points.
# 
# **Exercise 0** (10 points). Define a function, `UniqueCharacters(s)`, that given a string `s` returns a tuple of two elements: the first element is the number of unique alphabetic characters in the string and the second is the number of unique digits (base-10) in the string.
# 
# For example, the string `'ewwwffioj122434'` should output the following tuple: `(6, 4)`. The `6` occurs because there are 6 unique letters (`'e'`, `'w'`, `'f'`, `'i'`, `'o'`, and `'j'`) and `4` because there are 4 unique numbers (`'1'`,  `'2'`, `'3'`, `'4'`). Special characters may appear in the string but do not count as a letter or number.

# In[21]:


def UniqueCharacters(s):
    set_s = set(s)
    char_filter = [y for y in set_s if y.isalpha()]
    char_count = len(char_filter)
    num_filter = [y for y in set_s if y.isnumeric()] 
    num_count = len(num_filter)
    
    return (char_count, num_count)



# pythonic solution
def UniqueCharacters(s):
    return (len(set([i for i in s if i.isalpha()])),
           len(set([i for i in s if i.isdigit()])))

UniqueCharacters('ewwwffioj122434')


# In[22]:


# Test Cell: 'UniqueCharacters' (10 points)
assert UniqueCharacters('abc123') == (3,3)
assert UniqueCharacters('abc') == (3,0)
assert UniqueCharacters('aaa') == (1,0)
assert UniqueCharacters('aaa111') == (1,1)
assert UniqueCharacters('111') == (0,1)
assert UniqueCharacters('123') == (0,3)
assert UniqueCharacters('') == (0,0)
assert UniqueCharacters('///;;;...,????!!!!!###$$$%%%') == (0,0)
assert UniqueCharacters('//23bd') == (2,2)
assert UniqueCharacters('b2b3n4s4d9') == (4,4)
assert UniqueCharacters('9090909p0y90p90y90') == (2,2)
assert UniqueCharacters('ieowjfiojfioj2342io4ji') == (6,3)
assert UniqueCharacters('ewwwffioj122434') == (6,4)
assert UniqueCharacters('dwdj2ru3jf894jgf.,/23,4./3ei8fj2389ej89/,.,./2dd32je98dej89ij') == (9,5)
print("\n(Passed!)")


# **Fin!** You've reached the end of this problem. Don't forget to restart the
# kernel and run the entire notebook from top-to-bottom to make sure you did
# everything correctly. If that is working, try submitting this problem. (Recall
# that you *must* submit and pass the autograder to get credit for your work!)
