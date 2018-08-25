#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 22:36:39 2018

@author: zacholivier

Notebook 0 back up code
CSE6040 


Python review: Values, variables, types, lists, and strings
These first few notebooks are a set of exercises with two goals:
Review the basics of Python
Familiarize you with Jupyter


Regarding the first goal, these initial notebooks cover material we think you 
should already know from Chris Simpkins's Python Bootcamp from Fall 2018. 
This bootcamp is what students on the on-campus 
Georgia Tech MS Analytics students took.

Regarding the second goal, you'll observe that the bootcamp has each student 
install and work directly with the Python interpreter, which runs locally on 
his or her machine (e.g., see the Video: Getting Started link and Slide 7 of 
his Intro to Python slides). 
But in this course, we are using Jupyter Notebooks as the development environment.
 You can think of a Jupyter notebook as a web-based "skin" for running 
 a Python interpreter---possibly hosted on a remote server, 
 which is the case in this course. Here is a good tutorial on Jupyter.


Note for MS Analytics students. In this course we assume you are using 
Vocareum's deployment of Jupyter. You also have an option to use other 
Jupyter environments, including installing and running Jupyter on your 
own system. 
We can't provide technical support to you if you choose to go those routes, 
but if you'd like to do that anyway, we recommend Microsoft Azure Notebooks 
as a web-hosted option or the Continuum Analytics Anaconda distribution as a
 locally installed option.
 
 
 Study hint: Read the test code! You'll notice that most of the exercises 
 below have a place for you to code up your answer followed by a "test cell."
 That's a code cell that checks the output of your code to see whether it 
 appears to produce correct results. You can often learn a lot by reading 
 the test code. 
 In fact, sometimes it gives you a hint about how to approach the problem. 
 As such, we encourage you to try to read the test cells even if they seem cryptic,
 which is deliberate!


"""


# Exercise 0 (1 point). 
# Run the code cell below. 
# It should display the output string, Hello, world!.
print("Hello, world!")


# Exercise 1 (x_float_test: 1 point). 
# Create a variable named x_float whose numerical value is one (1) and whose 
# type is floating-point.
x_float = 1.0
x_float

# `x_float_test`: Test cell
assert x_float == 1
assert type(x_float) is float
print("\n(Passed!)")


# Exercise 2 (strcat_ba_test: 1 point). 
# Complete the following function, strcat_ba(a, b), so that given two strings, 
# a and b, it returns the concatenation of b followed by a 
# (pay attention to the order in these instructions!).
def strcat_ba(a, b):
    assert type(a) is str
    assert type(b) is str
    solution = b + a
    return solution


strcat_ba('john', 'jim')


# `strcat_ba_test`: Test cell

# Workaround:  # Python 3.5.2 does not have `random.choices()` (available in 3.6+)
def random_letter():
    from random import choice
    return choice('abcdefghijklmnopqrstuvwxyz')

def random_string(n, fun=random_letter):
    return ''.join([str(fun()) for _ in range(n)])

a = random_string(5)
b = random_string(3)
c = strcat_ba(a, b)
print('strcat_ba("{}", "{}") == "{}"'.format(a, b, c))
assert len(c) == len(a) + len(b)
assert c[:len(b)] == b
assert c[-len(a):] == a
print("\n(Passed!)")



# Exercise 3 (strcat_list_test: 2 points). Complete the following function, 
# strcat_list(L), which generalizes the previous function: given a list of 
# strings, L[:], returns the concatenation of the strings in reverse order. 
# For example:
#    strcat_list(['abc', 'def', 'ghi']) == 'ghidefabc'
def strcat_list(L):
    assert type(L) is list
    L_rev = list(reversed(L))
    L_concat = ''.join(L_rev)
    return L_concat
    
strcat_list(['abc', 'def', 'ghi'])

# `strcat_list_test`: Test cell
n = 3
nL = 6
L = [random_string(n) for _ in range(nL)]
Lc = strcat_list(L)

print('L == {}'.format(L))
print('strcat_list(L) == \'{}\''.format(Lc))
assert all([Lc[i*n:(i+1)*n] == L[nL-i-1] for i, x in zip(range(nL), L)])
print("\n(Passed!)")


# Exercise 4 (floor_fraction_test: 1 point). Suppose you are given two variables,
#  a and b, whose values are the real numbers,  a≥0
#   (non-negative) and  b>0
#  (positive). Complete the function, floor_fraction(a, b) so that it returns 
# ⌊ab⌋
# , that is, the floor of  ab
# . The type of the returned value must be int (an integer).

def is_number(x):
    """Returns `True` if `x` is a number-like type, e.g., `int`, `float`, `Decimal()`, ..."""
    from numbers import Number
    return isinstance(x, Number)
    
def floor_fraction(a, b):
    assert is_number(a) and a >= 0
    assert is_number(b) and b > 0
    floor = abs(a / b)
    return int(floor)

floor_fraction(1,4)



# `floor_fraction_test`: Test cell
from random import random
a = random()
b = random()
c = floor_fraction(a, b)

print('floor_fraction({}, {}) == floor({}) == {}'.format(a, b, a/b, c))
assert b*c <= a <= b*(c+1)
assert type(c) is int
print('\n(Passed!)')



#Exercise 5 (ceiling_fraction_test: 1 point). Complete the function, 
#ceiling_fraction(a, b), which for any numeric inputs, a and b, 
#corresponding to real numbers,  a≥0
#  and  b>0
# , returns  ⌈ab⌉
# , that is, the ceiling of  ab
# . The type of the returned value must be int.

def ceiling_fraction(a, b):
    assert is_number(a) and a >= 0
    assert is_number(b) and b > 0
    ceiling = -(-a // b)
    return int(ceiling)

check = ceiling_fraction(1,4)
type(check)


# `ceiling_fraction_test`: Test cell
from random import random
a = random()
b = random()
c = ceiling_fraction(a, b)
print('ceiling_fraction({}, {}) == ceiling({}) == {}'.format(a, b, a/b, c))
assert b*(c-1) <= a <= b*c
assert type(c) is int
print("\n(Passed!)")



# Exercise 6 (report_exam_avg_test: 1 point). Let a, b, and c represent three 
# exam scores as numerical values. Complete the function, 
# report_exam_avg(a, b, c) so that it computes the average score 
# (equally weighted) and returns the string, 'Your average score: XX', 
# where XX is the average rounded to one decimal place. 
# For example:
#    report_exam_avg(100, 95, 80) == 'Your average score: 91.7'

def report_exam_avg(a, b, c):
    assert is_number(a) and is_number(b) and is_number(c)
    test_list = [a,b,c]
    test_avg = round(float(sum(test_list) / len(test_list)),1)
    msg = str('Your average score: ' + str(test_avg))
    return msg



# `report_exam_avg_test`: Test cell
msg = report_exam_avg(100, 95, 80)
print(msg)
assert msg == 'Your average score: 91.7'

print("Checking some additional randomly generated cases:")
for _ in range(10):
    ex1 = random() * 100
    ex2 = random() * 100
    ex3 = random() * 100
    msg = report_exam_avg(ex1, ex2, ex3)
    ex_rounded_avg = float(msg.split()[-1])
    abs_err = abs(ex_rounded_avg*3 - (ex1 + ex2 + ex3)) / 3
    print("{}, {}, {} -> '{}' [{}]".format(ex1, ex2, ex3, msg, abs_err))
    assert abs_err <= 0.05

print("\n(Passed!)")



# Exercise 7 (count_word_lengths_test: 2 points). Write a function 
# count_word_lengths(s) that, given a string consisting of words separated by 
# spaces, returns a list containing the length of each word. Words will consist 
# of lowercase alphabetic characters, and they may be separated by multiple 
# consecutive spaces. 
# If a string is empty or has no spaces, the function should return an empty list.
# For instance, in this code sample, count_word_lengths
# ('the quick  brown   fox jumped over     the lazy  dog') == 
# [3, 5, 5, 3, 6, 4, 3, 4, 3]`
# the input string consists of nine (9) words whose respective lengths are
# shown in the list.

def count_word_lengths(s):
    assert all([x.isalpha() or x == ' ' for x in s])
    assert type(s) is str
    word_count = list(map(len, s.split()))
    return word_count

count_word_lengths('This is a great    class')




# `count_word_lengths_test`: Test cell

# Test 1: Example
qbf_str = 'the quick brown fox jumped over the lazy dog'
qbf_lens = count_word_lengths(qbf_str)
print("Test 1: count_word_lengths('{}') == {}".format(qbf_str, qbf_lens))
assert qbf_lens == [3, 5, 5, 3, 6, 4, 3, 4, 3]

# Test 2: Random strings
from random import choice # 3.5.2 does not have `choices()` (available in 3.6+)
#return ''.join([choice('abcdefghijklmnopqrstuvwxyz') for _ in range(n)])

def random_letter_or_space(pr_space=0.15):
    from random import choice, random
    is_space = (random() <= pr_space)
    if is_space:
        return ' '
    return random_letter()

S_LEN = 40
W_SPACE = 1 / 6
rand_str = random_string(S_LEN, fun=random_letter_or_space)
rand_lens = count_word_lengths(rand_str)
print("Test 2: count_word_lengths('{}') == '{}'".format(rand_str, rand_lens))
c = 0
while c < len(rand_str) and rand_str[c] == ' ':
    c += 1
for k in rand_lens:
    print("  => '{}'".format (rand_str[c:c+k]))
    assert (c+k) == len(rand_str) or rand_str[c+k] == ' '
    c += k
    while c < len(rand_str) and rand_str[c] == ' ':
        c += 1
    
# Test 3: Empty string
print("Test 3: Empty strings...")
assert count_word_lengths('') == []
assert count_word_lengths('   ') == []

print("\n(Passed!)")






#
#Exercise 0 (minmax_test: 1 point). Complete the function minmax(L), which 
#takes a list L and returns a pair---that is, 2-element Python tuple, 
#or "2-tuple"---whose first element is the minimum value in the list and whose
# second element is the maximum. 
# For instance:
#  minmax([8, 7, 2, 5, 1]) == (1, 8)

def minmax(L):
    assert hasattr(L, "__iter__")
    tup = (min(L), max(L))
    return tup
    
minmax([8,7,6,5])


# `minmax_test`: Test cell

L = [8, 7, 2, 5, 1]
mmL = minmax(L)
mmL_true = (1, 8)
print("minmax({}) -> {} [True: {}]".format(L, mmL, mmL_true))
assert type(mmL) is tuple and mmL == (1, 8)

from random import sample
L = sample(range(1000), 10)
mmL = minmax(L)
L_s = sorted(L)
mmL_true = (L_s[0], L_s[-1])
print("minmax({}) -> {} [True: {}]".format(L, mmL, mmL_true))
assert mmL == mmL_true

print("\n(Passed!)")

#
#Exercise 1 (remove_all_test: 2 points). Complete the function remove_all(L, x)
# so that, given a list L and a target value x, it returns a copy of the list
# that excludes all occurrences of x but preserves the order of the remaining
# elements. 
# For instance:
#    remove_all([1, 2, 3, 2, 4, 8, 2], 2) == [1, 3, 4, 8]
#Note.
# Your implementation should not modify the list being passed into remove_all.


def remove_all(L, x):
    assert type(L) is list and x is not None
    list_copy = [num for num in L if num != x]
    return list_copy

remove_all([1,2,3,2,4,5], 2)


# `remove_all_test`: Test cell
def test_it(L, x, L_ans):
    print("Testing `remove_all({}, {})`...".format(L, x))
    print("\tTrue solution: {}".format(L_ans))
    L_copy = L.copy()
    L_rem = remove_all(L_copy, x)
    print("\tYour computed solution: {}".format(L_rem))
    assert L_copy == L, "Your code appears to modify the input list."
    assert L_rem == L_ans, "The returned list is incorrect."

# Test 1: Example
test_it([1, 2, 3, 2, 4, 8, 2], 2, [1, 3, 4, 8])

# Test 2: Random list
from random import randint
target = randint(0, 9)
L_input = []
L_ans = []
for _ in range(20):
    v = randint(0, 9)
    L_input.append(v)
    if v != target:
        L_ans.append(v)
test_it(L_input, target, L_ans)

print("\n(Passed!)")



#Exercise 2 (compress_vector_test: 2 points). Suppose you are given a vector, x,
# containing real values that are mostly zero. For instance:
#    x = [0.0, 0.87, 0.0, 0.0, 0.0, 0.32, 0.46, 0.0, 0.0, 0.10, 0.0, 0.0]
#Complete the function, compress_vector(x), so that returns a dictionary d 
#with two keys, d['inds'] and d['vals'], which are lists that indicate the 
#position and value of all the non-zero entries of x. For the previous example,
#    d['inds'] = [1, 5, 6, 9]
#    d['vals'] = [0.87, 0.32, 0.46, 0.10]
#Note 1. Your implementation must not modify the input vector x.
#Note 2. If x contains only zero entries, d['inds'] and d['vals'] should be empty lists.


def compress_vector(x):
    assert type(x) is list
    d = {'inds': [], 'vals': []}
    d['inds'] = [i for i, e in enumerate(x) if e != 0]
    d['vals'] = [i for i in x if i != 0]
    return d


compress_vector(x = [0,0,0,1,0])




# `compress_vector_test`: Test cell
def check_compress_vector(x_orig):
    print("Testing `compress_vector(x={})`:".format(x_orig))
    x = x_orig.copy()
    nz = x.count(0.0)
    print("\t`x` has {} zero entries.".format(nz))
    d = compress_vector(x)
    print("\tx (after call): {}".format(x))
    print("\td: {}".format(d))
    assert x == x_orig, "Your implementation appears to modify the input."
    assert type(d) is dict, "Output type is not `dict` (a dictionary)."
    assert 'inds' in d and type(d['inds']) is list, "Output key, 'inds', does not have a value of type `list`."
    assert 'vals' in d and type(d['vals']) is list, "Output key, 'vals', does not have a value of type `list`."
    assert len(d['inds']) == len(d['vals']), "`d['inds']` and `d['vals']` are lists of unequal length."
    for i, v in zip(d['inds'], d['vals']):
        assert x[i] == v, "x[{}] == {} instead of {}".format(i, x[i], v)
    assert nz + len(d['vals']) == len(x), "Output may be missing values."
    assert len(d.keys()) == 2, "Output may have keys other than 'inds' and 'vals'."
    
# Test 1: Example
x = [0.0, 0.87, 0.0, 0.0, 0.0, 0.32, 0.46, 0.0, 0.0, 0.10, 0.0, 0.0]
check_compress_vector(x)

# Test 2: Random sparse vectors
from random import random
for _ in range(3):
    print("")
    x = []
    for _ in range(20):
        if random() <= 0.8: # Make about 10% of entries zero
            v = 0.0
        else:
            v = float("{:.2f}".format(random()))
        x.append(v)
    check_compress_vector(x)
    
# Test 3: Empty vector
x = [0.0] * 10
check_compress_vector(x)

print("\n(Passed!)")



#Repeated indices. 
#Consider the compressed vector data structure, d, in the preceding exercise, 
#which stores a list of indices (d['inds']) and a list of values (d['vals']).
#Suppose we allow duplicate indices, possibly with different values.
# For example:
#    d['inds'] == [0,   3,   7,   3,   3,   5, 1]
#    d['vals'] == [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
#In this case, the index 3 appears three times. 
#(Also note that the indices d['ind'] need not appear in sorted order.)
#Let's adopt the convention that when there are repeated indices, the "true" 
#value there is the sum of the individual values. 
#In other words, the true vector corresponding to this example of d would be:
#    # ind:  0    1    2    3*    4    5    6    7
#    x == [1.0, 7.0, 0.0, 11.0, 0.0, 6.0, 0.0, 3.0]


#Exercise 3 (decompress_vector_test: 2 points). Complete the function 
#decompress_vector(d) that takes a compressed vector d, which is a dictionary 
#with keys for the indices (inds) and values (vals), and returns the 
#corresponding full vector. For any repeated index, the values should be summed.
#The function should accept an optional parameter, n, 
#that specifies the length of the full vector. You may assume this length is 
#at least max(d['inds'])+1.


    
# Test 1: Example
d = {}
d['inds'] = [0,   3,   7,   3,   3,   5, 1]
d['vals'] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
x_true = [1.0, 7.0, 0.0, 11.0, 0.0, 6.0, 0.0, 3.0]



def decompress_vector(d, n=None):
    # Checks the input
    assert type(d) is dict and 'inds' in d and 'vals' in d, "Not a dictionary or missing keys"
    assert type(d['inds']) is list and type(d['vals']) is list, "Not a list"
    assert len(d['inds']) == len(d['vals']), "Length mismatch"
    
    # Determine length of the full vector
    i_max = max(d['inds']) if d['inds'] else -1
    
    d['x_true'] = set(d['inds'], d['vals'])
    
    return d['x_true']
                



decompress_vector(d)

dict(zip(d['inds'], d['vals']))

s = (set(d['inds']))
d = dict.fromkeys(s, 0)


#Exercise 4 (find_common_inds_test: 1 point). 
#Suppose you are given two compressed vectors, d1 and d2, each represented 
#as described above and possibly with repeated indices. 
#Complete the function find_common_inds(d1, d2) so that it returns a list of 
#the indices they have in common.
#For instance, suppose:
#    d1 == {'inds': [9, 9, 1, 9, 8, 1], 'vals': [0.28, 0.84, 0.71, 0.03, 0.04, 0.75]}
#    d2 == {'inds': [0, 9, 9, 1, 3, 3, 9], 'vals': [0.26, 0.06, 0.46, 0.58, 0.42, 0.21, 0.53, 0.76]}
#Then:
#    find_common_inds(d1, d2) == [1, 9]
#Note 1. The returned list must not have duplicate indices, even if the inputs do. In the example, the index 9 is repeated in both d1 and d2, but the output includes just one 9.
#Note 2. In the returned list, the order of indices does not matter. For instance, the example shows [1, 9] but [9, 1] would also be valid.



    
d1 = {'inds': [9, 9, 1, 9, 8, 1], 'vals': [0.28, 0.84, 0.71, 0.03, 0.04, 0.75]}
d2 = {'inds': [0, 9, 9, 1, 3, 3, 9], 'vals': [0.26, 0.06, 0.46, 0.58, 0.42, 0.21, 0.53, 0.76]}
ans = [1, 9]




def find_common_inds(d1, d2):
    assert type(d1) is dict and 'inds' in d1 and 'vals' in d1
    assert type(d2) is dict and 'inds' in d2 and 'vals' in d2
    intersect_dict = []
    for i in d1['inds']:
        if i in d2['inds']:
            intersect_dict.append(i)
    return list(set(intersect_dict))

find_common_inds(d1, d2)
            
            
#Consider the following dataset of exam grades, 
#organized as a 2-D table and stored in Python as a "list of lists" 
#under the variable name, grades.

grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]



students = [item[0] for item in grades[1:]]

# `students_test`: Test cell
print(students)
assert type(students) is list
assert students == ['Thorny', 'Mac', 'Farva', 'Rabbit', 'Ursula', 'Foster']
print("\n(Passed!)")




#Exercise 1 (assignments_test: 1 point). Write some code to compute a new list 
#named assignments[:], to hold the names of the class assignments. 
#(These appear in the descriptive header element of grades.)
assignments = grades[0]
assignments = assignments[1:]

# `assignments_test`: Test cell
print(assignments)
assert type(assignments) is list
assert assignments == ['Exam 1', 'Exam 2', 'Exam 3']
print("\n(Passed!)")


#Exercise 2 (grade_lists_test: 1 point). Write some code to compute a 
#new dictionary, named grade_lists, that maps names of students to lists of 
#their exam grades. 
#The grades should be converted from strings to integers. 
#For instance, grade_lists['Thorny'] == [100, 90, 80].

grade_lists = {}



grade_only = grades[1:]


a = grade_only[0]
b = grade_only[1]
c = grade_only[2]
d = grade_only[3]
e = grade_only[4]
f = grade_only[5]

grade_lists['Thorny'] = a[1:]
grade_lists['Mac'] = b[1:]
grade_lists['Farva'] = c[1:]
grade_lists['Rabbit'] = d[1:]
grade_lists['Ursula'] = e[1:]
grade_lists['Foster'] = f[1:]



len(grades) - 1 == len(grade_lists)

grade_lists = {k: list(map(int, v)) for k, v in grade_lists.items()}




# `grade_lists_test`: Test cell
print(grade_lists)
assert type(grade_lists) is dict, "Did not create a dictionary."
assert len(grade_lists) == len(grades)-1, "Dictionary has the wrong number of entries."
assert {'Thorny', 'Mac', 'Farva', 'Rabbit', 'Ursula', 'Foster'} == set(grade_lists.keys()), "Dictionary has the wrong keys."
assert grade_lists['Thorny'] == [100, 90, 80], 'Wrong grades for: Thorny'
assert grade_lists['Mac'] == [88, 99, 111], 'Wrong grades for: Mac'
assert grade_lists['Farva'] == [45, 56, 67], 'Wrong grades for: Farva'
assert grade_lists['Rabbit'] == [59, 61, 67], 'Wrong grades for: Rabbit'
assert grade_lists['Ursula'] == [73, 79, 83], 'Wrong grades for: Ursula'
assert grade_lists['Foster'] == [89, 97, 101], 'Wrong grades for: Foster'
print("\n(Passed!)")




#Exercise 3 (grade_dicts_test: 2 points). Write some code to compute a new 
#dictionary, grade_dicts, that maps names of students to dictionaries 
#containing their scores. Each entry of this scores dictionary should be 
#keyed on assignment name and hold the corresponding grade as an integer. 
#For instance, grade_dicts['Thorny']['Exam 1'] == 100.


grades


grade_dicts = {}



grade_only = grades[1:]


a = grade_only[0]
b = grade_only[1]
c = grade_only[2]
d = grade_only[3]
e = grade_only[4]
f = grade_only[5]



grade_dicts['Thorny'] = {
        'Exam 1':int(a[1]), 'Exam 2': int(a[2]), 'Exam 3': int(a[3])
        }
    
grade_dicts['Mac'] = {
        'Exam 1':int(b[1]), 'Exam 2': int(b[2]), 'Exam 3': int(b[3])
        }

grade_dicts['Farva'] = {
        'Exam 1':int(c[1]), 'Exam 2': int(c[2]), 'Exam 3': int(c[3])
        }

grade_dicts['Rabbit'] = {
        'Exam 1':int(d[1]), 'Exam 2': int(d[2]), 'Exam 3': int(d[3])
        }

grade_dicts['Ursula'] = {
        'Exam 1':int(e[1]), 'Exam 2': int(e[2]), 'Exam 3': int(e[3])
        }

grade_dicts['Foster'] = {
        'Exam 1':int(f[1]), 'Exam 2': int(f[2]), 'Exam 3': int(f[3])
        }
    


grade_dicts['Thorny']['Exam 1']





# `grade_dicts_test`: Test cell
print(grade_dicts)
assert type(grade_dicts) is dict, "Did not create a dictionary."
assert len(grade_dicts) == len(grades)-1, "Dictionary has the wrong number of entries."
assert {'Thorny', 'Mac', 'Farva', 'Rabbit', 'Ursula', 'Foster'} == set(grade_dicts.keys()), "Dictionary has the wrong keys."
assert grade_dicts['Foster']['Exam 1'] == 89, 'Wrong score'
assert grade_dicts['Foster']['Exam 3'] == 101, 'Wrong score'
assert grade_dicts['Foster']['Exam 2'] == 97, 'Wrong score'
assert grade_dicts['Ursula']['Exam 1'] == 73, 'Wrong score'
assert grade_dicts['Ursula']['Exam 3'] == 83, 'Wrong score'
assert grade_dicts['Ursula']['Exam 2'] == 79, 'Wrong score'
assert grade_dicts['Rabbit']['Exam 1'] == 59, 'Wrong score'
assert grade_dicts['Rabbit']['Exam 3'] == 67, 'Wrong score'
assert grade_dicts['Rabbit']['Exam 2'] == 61, 'Wrong score'
assert grade_dicts['Mac']['Exam 1'] == 88, 'Wrong score'
assert grade_dicts['Mac']['Exam 3'] == 111, 'Wrong score'
assert grade_dicts['Mac']['Exam 2'] == 99, 'Wrong score'
assert grade_dicts['Farva']['Exam 1'] == 45, 'Wrong score'
assert grade_dicts['Farva']['Exam 3'] == 67, 'Wrong score'
assert grade_dicts['Farva']['Exam 2'] == 56, 'Wrong score'
assert grade_dicts['Thorny']['Exam 1'] == 100, 'Wrong score'
assert grade_dicts['Thorny']['Exam 3'] == 80, 'Wrong score'
assert grade_dicts['Thorny']['Exam 2'] == 90, 'Wrong score'
print("\n(Passed!)")




#Exercise 4 (avg_grades_by_student_test: 1 point). Write some code to compute 
#a dictionary named avg_grades_by_student that maps each student to his 
#or her average exam score. 
#For instance, avg_grades_by_student['Thorny'] == 90.
#Hint. The statistics module of Python has at least one helpful function.

from statistics import mean

avg_grades_by_student = {}

for k in grade_dicts.items():
    name = k[0]
    df = k[1]
    avg_grade = mean(df.values())
    d1 = {name:avg_grade}
    
    avg_grades_by_student.update(d1)
    
avg_grades_by_student['Thorny']
    
len(students)

#del avg_grades_by_student
    

# `avg_grades_by_student_test`: Test cell
print(avg_grades_by_student)
assert type(avg_grades_by_student) is dict, "Did not create a dictionary."
assert len(avg_grades_by_student) == len(students), "Output has the wrong number of students."
assert abs(avg_grades_by_student['Mac'] - 99.33333333333333) <= 4e-15, 'Mean is incorrect'
assert abs(avg_grades_by_student['Foster'] - 95.66666666666667) <= 4e-15, 'Mean is incorrect'
assert abs(avg_grades_by_student['Farva'] - 56) <= 4e-15, 'Mean is incorrect'
assert abs(avg_grades_by_student['Rabbit'] - 62.333333333333336) <= 4e-15, 'Mean is incorrect'
assert abs(avg_grades_by_student['Thorny'] - 90) <= 4e-15, 'Mean is incorrect'
assert abs(avg_grades_by_student['Ursula'] - 78.33333333333333) <= 4e-15, 'Mean is incorrect'
print("\n(Passed!)")



#Exercise 5 (grades_by_assignment_test: 2 points). 
#Write some code to compute a dictionary named grades_by_assignment, 
#whose keys are assignment (exam) names and whose values are lists of 
#scores over all students on that assignment. 
#For instance, grades_by_assignment['Exam 1'] == [100, 88, 45, 59, 73, 89].

#from collections import defaultdict, OrderedDict

d = {'Exam 1': [], 'Exam 2': [], 'Exam 3': []}



for k in grade_dicts.values():
    for j, v in k.items():
        d[j].append(v)

grades_by_assignment = dict(d)

grades_by_assignment['Exam 1']

# `grades_by_assignment_test`: Test cell
print(grades_by_assignment)
assert type(grades_by_assignment) is dict, "Output is not a dictionary."
assert len(grades_by_assignment) == 3, "Wrong number of assignments."
assert grades_by_assignment['Exam 1'] == [100, 88, 45, 59, 73, 89], 'Wrong grades list'
assert grades_by_assignment['Exam 3'] == [80, 111, 67, 67, 83, 101], 'Wrong grades list'
assert grades_by_assignment['Exam 2'] == [90, 99, 56, 61, 79, 97], 'Wrong grades list'
print("\n(Passed!)")









#Exercise 6 (avg_grades_by_assignment_test: 1 point). 
#Write some code to compute a dictionary, 
#avg_grades_by_assignment, which maps each exam to its average score.

avg_grades_by_assignment = {}

for key, value in grades_by_assignment.items():
    name = key
    vals = value
    avg_vals = mean(vals)
    d = {name : avg_vals}
    
    avg_grades_by_assignment.update(d)
    
    
print(avg_grades_by_assignment)

# `avg_grades_by_assignment_test`: Test cell
print(avg_grades_by_assignment)
assert type(avg_grades_by_assignment) is dict
assert len(avg_grades_by_assignment) == 3
assert abs((100+88+45+59+73+89)/6 - avg_grades_by_assignment['Exam 1']) <= 7e-15
assert abs((80+111+67+67+83+101)/6 - avg_grades_by_assignment['Exam 3']) <= 7e-15
assert abs((90+99+56+61+79+97)/6 - avg_grades_by_assignment['Exam 2']) <= 7e-15
print("\n(Passed!)")


#Exercise 7 (rank_test: 2 points). Write some code to create a new list, rank,
# which contains the names of students in order by decreasing score. 
# That is, rank[0] should contain the name of the top student 
# (highest average exam score), and rank[-1] should have the name of the 
# bottom student (lowest average exam score).

avg_grades_by_student

rank = sorted(
        avg_grades_by_student,
        key = avg_grades_by_student.get,
        reverse = True
        )



rank[0]
rank[-1]


# `rank_test`: Test cell
print(rank)
print("\n=== Ranking ===")
for i, s in enumerate(rank):
    print("{}. {}: {}".format(i+1, s, avg_grades_by_student[s]))
    
assert rank == ['Mac', 'Foster', 'Thorny', 'Ursula', 'Rabbit', 'Farva']
for i in range(len(rank)-1):
    assert avg_grades_by_student[rank[i]] >= avg_grades_by_student[rank[i+1]]
print("\n(Passed!)")