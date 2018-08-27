#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 21:28:55 2018

@author: zacholivier


Association rule mining
In this notebook, you'll implement the basic pairwise association rule mining 
algorithm.

To keep the implementation simple, you will apply your implementation to 
a simplified dataset, namely, letters ("items") in words 
("receipts" or "baskets"). Having finished that code, you will then apply 
that code to some grocery store market basket data. If you write the code well,
 it will not be difficult to reuse building blocks from the letter case in 
 the basket data case.
 
Problem definition
Let's say you have a fragment of text in some language. You wish to know 
whether there are association rules among the letters that appear in a word. 
In this problem:
Words are "receipts"
Letters within a word are "items"
You want to know whether there are association rules of the form, a⟹b
, where a
 and b
 are letters. You will write code to do that by calculating for each rule its
 confidence, conf(a⟹b)
. "Confidence" will be another name for an estimate of the conditional 
probability of b
 given a
, or Pr[b|a]
.

    
"""



#Sample text input
#Let's carry out this analysis on a "dummy" text fragment, which graphic 
#designers refer to as the lorem ipsum:


latin_text = """
Sed ut perspiciatis, unde omnis iste natus error sit
voluptatem accusantium doloremque laudantium, totam
rem aperiam eaque ipsa, quae ab illo inventore
veritatis et quasi architecto beatae vitae dicta
sunt, explicabo. Nemo enim ipsam voluptatem, quia
voluptas sit, aspernatur aut odit aut fugit, sed
quia consequuntur magni dolores eos, qui ratione
voluptatem sequi nesciunt, neque porro quisquam est,
qui dolorem ipsum, quia dolor sit amet consectetur
adipisci[ng] velit, sed quia non numquam [do] eius
modi tempora inci[di]dunt, ut labore et dolore
magnam aliquam quaerat voluptatem. Ut enim ad minima
veniam, quis nostrum exercitationem ullam corporis
suscipit laboriosam, nisi ut aliquid ex ea commodi
consequatur? Quis autem vel eum iure reprehenderit,
qui in ea voluptate velit esse, quam nihil molestiae
consequatur, vel illum, qui dolorem eum fugiat, quo
voluptas nulla pariatur?

At vero eos et accusamus et iusto odio dignissimos
ducimus, qui blanditiis praesentium voluptatum
deleniti atque corrupti, quos dolores et quas
molestias excepturi sint, obcaecati cupiditate non
provident, similique sunt in culpa, qui officia
deserunt mollitia animi, id est laborum et dolorum
fuga. Et harum quidem rerum facilis est et expedita
distinctio. Nam libero tempore, cum soluta nobis est
eligendi optio, cumque nihil impedit, quo minus id,
quod maxime placeat, facere possimus, omnis voluptas
assumenda est, omnis dolor repellendus. Temporibus
autem quibusdam et aut officiis debitis aut rerum
necessitatibus saepe eveniet, ut et voluptates
repudiandae sint et molestiae non recusandae. Itaque
earum rerum hic tenetur a sapiente delectus, ut aut
reiciendis voluptatibus maiores alias consequatur
aut perferendis doloribus asperiores repellat.
"""

print("First 100 characters:\n  {} ...".format(latin_text[:100]))




#Data cleaning. Like most data in the real world, this dataset is noisy. 
#It has both uppercase and lowercase letters, words have repeated letters, 
#and there are all sorts of non-alphabetic characters. For our analysis, 
#we should keep all the letters and spaces (so we can identify distinct words),
# but we should ignore case and ignore repetition within a word.
#
#For example, the eighth word of this text is "error." As an itemset, it 
#consists of the three unique letters,  {e,o,r}
# . That is, treat the word as a set, meaning you only keep the unique letters.
#This itemset has three possible itempairs:  {e,o}
# ,  {e,r}
# , and  {o,r}
# .
#Start by writing some code to help "clean up" the input.

#Exercise 1 (normalize_string_test: 2 points). Complete the following function,
# normalize_string(s). The input s is a string (str object). The function 
# should return a new string with (a) all characters converted to lowercase 
# and (b) all non-alphabetic, non-whitespace characters removed.
 
 
#Clarification. 
#Scanning the sample text, latin_text, you may see things that 
#look like special cases. For instance, inci[di]dunt and [do]. For these, 
#simply remove the non-alphabetic characters and only separate the words if 
#there is explicit whitespace.
#For instance, inci[di]dunt would become incididunt (as a single word) and 
#[do] would become do as a standalone word because the original string has 
#whitespace on either side. A period or comma without whitespace would, 
#similarly, just be treated as a non-alphabetic character inside a word unless
# there is explicit whitespace. So e pluribus.unum basium would become e 
# pluribusunum basium even though your common-sense understanding might 
# separate pluribus and unum.
#Hint. Regard as a whitespace character anything "whitespace-like." 
#That is, consider not just regular spaces, but also tabs, newlines, and 
#perhaps others. To detect whitespaces easily, look for a "high-level" function
# that can help you do so rather than checking for literal space characters.



import re

def normalize_string(s):
    assert type (s) is str
    lower_string = s.lower()
    clean_string = re.sub(r'[^\w\s]', '', lower_string)
    return clean_string
    
# Demo:
print(latin_text[:100], "...\n=>", normalize_string(latin_text[:100]), "...")

norm_latin_text = normalize_string(latin_text)
len(norm_latin_text)


# `normalize_string_test`: Test cell
norm_latin_text = normalize_string(latin_text)

assert type(norm_latin_text) is str
assert len(norm_latin_text) == 1694
assert all([c.isalpha() or c.isspace() for c in norm_latin_text])
assert norm_latin_text == norm_latin_text.lower()

print("\n(Passed!)")


#Exercise 2 (get_normalized_words_test: 1 point). Implement the following 
#function, get_normalized_words(s). It takes as input a string s 
#(i.e., a str object). It should return a list of the words in s, after 
#normalization per the definition of normalize_string(). 
#(That is, the input s may not be normalized yet.)

def get_normalized_words (s):
    assert type (s) is str
    s = normalize_string(s)
    split_words = s.split()
    return split_words
    

# Demo:
print ("First five words:\n{}".format (get_normalized_words (latin_text)[:5]))

get_normalized_words(latin_text)

# `get_normalized_words_test`: Test cell
norm_latin_words = get_normalized_words(norm_latin_text)

assert len(norm_latin_words) == 250
for i, w in [(20, 'illo'), (73, 'eius'), (144, 'deleniti'), (248, 'asperiores')]:
    assert norm_latin_words[i] == w

print ("\n(Passed.)")



#Exercise 3 (make_itemsets_test: 2 points). Implement a function, 
#make_itemsets(words). The input, words, is a list of strings. 
#Your function should convert the characters of each string into an itemset 
#and then return the list of all itemsets. These output itemsets should appear
# in the same order as their corresponding words in the input.

from collections import OrderedDict

def make_itemsets(words):
    
    sets_word = []
    
    for word in words:
        s = ''.join(OrderedDict.fromkeys(word).keys())
        s = s.strip()
        sets_word.append(set(s))
    return sets_word

# `make_itemsets_test`: Test cell
make_itemsets(norm_latin_words)


# `make_itemsets_test`: Test cell
norm_latin_itemsets = make_itemsets(norm_latin_words)

# Lists should have the same size
assert len(norm_latin_itemsets) == len(norm_latin_words)

# Test a random sample
from random import sample
for i in sample(range(len(norm_latin_words)), 5):
    print('[{}]'.format(i), norm_latin_words[i], "-->", norm_latin_itemsets[i])
    assert set(norm_latin_words[i]) == norm_latin_itemsets[i]
print("\n(Passed!)")


















'''
Implementing the basic algorithm
Recall the pseudocode for the algorithm that Rachel and Rich derived together:
FindAssocRules (pseudocode)
In the following series of exercises, let's implement this method. 
We'll build it "bottom-up," first defining small pieces and working our way 
toward the complete algorithm. This method allows us to test each piece before
 combining them.
Observe that the bulk of the work in this procedure is just updating these
 tables,  T and  C. 
 So your biggest implementation decision is how to store those. 
 A good choice is to use a dictionary


Aside: Default dictionaries
Recall that the overall algorithm requires maintaining a table of item-pair
 (tuples) counts. It would be convenient to use a dictionary to store this 
 table, where keys refer to item-pairs and the values are the counts.
However, with Python's built-in dictionaries, you always to have to check 
whether a key exists before updating it. For example, consider this code 
fragment:
    
D = {'existing-key': 5} # Dictionary with one key-value pair

D['existing-key'] += 1 # == 6
D['new-key'] += 1  # Error: 'new-key' does not exist!
The second attempt causes an error because 'new-key' is not yet a member of 
the dictionary. So, a more correct approach would be to do the following:
    
D = {'existing-key': 5} # Dictionary with one key-value pair

if 'existing-key' not in D:
    D['existing-key'] = 0
D['existing-key'] += 1

if 'new-key' not in D:
    D['new-key'] = 0
D['new-key'] += 1
This pattern is so common that there is a special form of dictionary, called 
a default dictionary, which is available from the collections module: 
    collections.defaultdict.
When you create a default dictionary, you need to provide a "factory" function
 that the dictionary can use to create an initial value when the key does not
 exist. For instance, in the preceding example, when the key was not present 
 the code creates a new key with the initial value of an integer zero (0).
 Indeed, this default value is the one you get when you call int() with no 
 arguments:

'''

print (int ())

from collections import defaultdict

D2 = defaultdict (int) # Empty dictionary

D2['existing-key'] = 5 # Create one key-value pair

D2['existing-key'] += 1 # Update
D2['new-key'] += 1

print (D2)



#Exercise 4 (update_pair_counts_test: 2 points). Start by implementing a 
#function that enumerates all item-pairs within an itemset and updates, 
#in-place, a table that tracks the counts of those item-pairs.
#The signature of this function is:
#   def update_pair_counts(pair_counts, itemset):
#where you pair_counts is the table to update and itemset is the itemset 
#from which you need to enumerate item-pairs. You may assume pair_counts 
#is a default dictionary. Each key is a pair of items (a, b), and each value
# is the count. You may assume all items in itemset are distinct, i.e., 
# that you may treat it as you would any set-like collection. Since the 
# function will modify pair_counts, it does not need to return an object.

from collections import defaultdict
from itertools import combinations # Hint!

def update_pair_counts (pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type (pair_counts) is defaultdict

    #
    # YOUR CODE HERE
    #



# `update_pair_counts_test`: Test cell
itemset_1 = set("error")
itemset_2 = set("dolor")
pair_counts = defaultdict(int)

update_pair_counts(pair_counts, itemset_1)
assert len(pair_counts) == 6
update_pair_counts(pair_counts, itemset_2)
assert len(pair_counts) == 16

print('"{}" + "{}"\n==> {}'.format (itemset_1, itemset_2, pair_counts))
for a, b in pair_counts:
    assert (b, a) in pair_counts
    assert pair_counts[(a, b)] == pair_counts[(b, a)]
    
print ("\n(Passed!)")



























