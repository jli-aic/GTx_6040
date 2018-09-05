
# coding: utf-8

# # Problem 7
# 
# **Letter frequencies.** This problem has three (3) exercises worth a total of ten (10) points.

# Letter frequency in text has been studied in cryptoanalysis, in particular frequency analysis. Linguists use letter frequency analysis as a rudimentary technique for language identification, where it's particularly effective as an indicator of whether an unknown writing system is alphabetic, syllablic, or ideographic.
# 
# Primarily, three different ways exist for letter frequency analysis. Each way generally results in very different charts for common letters. Based on the provided text, the first method is to count letter frequency in root words of a dictionary. The second way is to include all word variants when counting, such as gone, going and goes and not just the root word go. Such a system results in letters like "s" appearing much more frequently. The last variant is to count letters based on their frequency in the actual text that is being studied. 
# 
# For more details, refer to the link: 
# https://en.wikipedia.org/wiki/Letter_frequency
# 
# In this problem, we will focus on the 3rd methodology.

# **Exercise 0** (2 points). First, given a string input, define a function  `preprocess` that returns a string with non-alphabetic characters removed and all the alphabets converted into a lower case. 
# 
# For example, 'We are coding letter Frequency! Yay!" would be transformed into "wearecodingletterfrequencyyay"

# In[6]:


def preprocess(S):
    s = ''.join([c.lower() for c in S if c.isalpha()])
    return s


# In[7]:


# Test cell: valid_string
import random, string

N_str = 100 #Length of random string

def generate_str(n):
    random_str = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for _ in range(n))
    return random_str

def check_preprocess_str(n):
    random_str = generate_str(n)
    print("Input String: ",random_str)
    assert preprocess('random_str').islower() == True
    assert preprocess(random_str).isalpha() == True
    print("|----Your function seems to work correct for the string----|"+"\n")

check_preprocess_str(N_str)
check_preprocess_str(N_str)
check_preprocess_str(N_str)

print("\n(Passed)!")


# **Exercise 1** (4 points). With the necessary pre-processing complete, the next step is to write a function `count_letters(S)` to count the number of occurrences of each letter in the alphabet.  
# 
# You can assume that only letters will be present in the input string. It should output a dictionary and if any alphabet (a-z) is missing in the input string, it should still be a part of the output dictionary and its corresponding value should be equal to zero.
# 

# In[8]:


import random

def count_letters(S):
    alphabet = string.ascii_lowercase
    count_dict = {c: S.count(c) for c in alphabet}
    return count_dict


# In[9]:


# Test cell: count_letters
import collections

N_processed_str = 100

def generate_processed_str(n):
    random_processed_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    return random_processed_str

def check_count_letters(S):
    print("Input String: ",S)
    random_char = chr(random.randint(97,122))
    print("Character frequency evaluated for: ", random_char)
    if(random_char in S):
        assert count_letters(S)[random_char] == collections.Counter(S)[random_char]
        print("|----Your function seems to return correct freq for the char----|"+"\n")
    else:
        assert count_letters(S)[random_char] == 0
        print("|----Your function seems to return correct freq for the char----|"+"\n")
        
check_count_letters(generate_processed_str(N_processed_str))
check_count_letters(generate_processed_str(N_processed_str))
check_count_letters(generate_processed_str(N_processed_str))
print("\n(Passed)!")


# **Exercise 2** (4 points). The next step is to sort the distribution of a dictionary containing all the letters in the alphabet as keys and number of occurrences in text as associated value. 
# 
# Sorting should be first done in decreasing order by occurrence count and for two elements with same count, the order should be alphabetic. The function  `find_top_letter(d)` should return the 1st character in the order.

# In[13]:


def find_top_letter(d):
    t = [(l, o) for l,o in d.items()] # change items in dict to a list
    t.sort(key = lambda x: (x[1]*-1, x[0]))
    return t[:1][0][0]
    


# In[14]:


# Test cell: highest_freq_letter

def create_random_dict():
    max_char_value = random.randint(5, 20)
    random_dict = {c:random.randint(0,max_char_value-1) for c in string.ascii_lowercase}
    random_letter1, random_letter2 = random.sample(string.ascii_lowercase, 2)
    random_dict[random_letter1], random_dict[random_letter2] = max_char_value, max_char_value
    if(random_letter1 < random_letter2):
        return random_letter1, random_dict
    else:
        return random_letter2, random_dict

def check_top_letter():
    top_letter, random_dict = create_random_dict()
    user_letter = find_top_letter(random_dict)
    assert user_letter == top_letter
    print("Input Dictionary: ", random_dict)
    print("Your function correctly returned most frequent letter: {} \n".format(user_letter))
    
check_top_letter()
check_top_letter()
check_top_letter()
print("\n(Passed)!")


# **Fin!** You've reached the end of this problem. Don't forget to restart the kernel and run the entire notebook from top-to-bottom to make sure you did everything correctly. If that is working, try submitting this problem. (Recall that you *must* submit and pass the autograder to get credit for your work!)
