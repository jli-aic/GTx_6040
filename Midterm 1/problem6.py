
# coding: utf-8

# # Problem 6: Hash Tables

# You've used Python's `dict` data type extensively now. Recall that it maps keys to values. But how is it implemented under-the-hood? One way is via a classic computer science technique known as a **hash table**.
# 
# For our purposes, a hash table has two parts:
# 
# 1. A list of **buckets**. The buckets are stored in a Python `list` of a certain maximum size. Each bucket has a **bucket ID**, which is its position in the list of buckets. Each bucket is itself _another_ Python list, which will hold the values. But more on that detail later (under **Collisions**, below).
# 2. A **hash function**, which converts any given key into the bucket ID in which it belongs. We'll sometimes refer to the output of the hash function as the **hash value** of the given key.
# 
# The hash function is usually decomposed into two steps. The first step converts the key into some non-negative integer, which may be very large. So, we can take this large integer _modulo_ the number of buckets, to get a valid bucket ID. (Recall that $a$ modulo $b$ means the remainder after dividing $a$ by $b$, which in Python you can compute using the `%` operator.)

# In this problem, you will implement a hash table that maps names (the keys, given as strings) to phone numbers (the values). You may find it helpful to keep the following image in mind when reasoning about how a hash table works. First, suppose you have 16 `buckets`:
# 
# ![alt text](https://upload.wikimedia.org/wikipedia/commons/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg "Hash Table add() Function")
# 
# Further suppose that the first step of our hash function calculates the value of 124,722 for the key, `John Smith`. We would then take this value `modulo 16`, the size of `buckets`, and are left with the bucket ID of `124722 % 16 == 2`. We put John's information in this bucket, which is location 2 in our list of buckets.
# 
# What is the motivation for this scheme? **If** the hash function does a good job of spreading out keys among the buckets, then the average time it takes to find a value into the hash table will be proportional to the average bucket size, rather than being proportional to the size of the entire list. And if we have enough buckets, then each bucket will (hopefully) be small, so that searching the bucket will be fast even if we use brute force.
# 
# > *One detail.* Unlike the image above, in this problem you will store *both* the key and value into the hash table. That is, you will be inserting `(key, value)` pairs into the buckets, instead of just the value as shown in the illustration above.

# ** Exercise 0 (2 points)**: There are many ways to compute a hash value for a string. We want a method that will add an element of uniqueness for each string, so that any two strings have a small likelihood of being hashed to the same value. One way to do that is to calculate a value of this form, for a given string `s`:
# 
# $$
# \mbox{HashFunction}(s) = \left(\mbox{InitialValue} \:+ \sum_{i=0}^{\mbox{len}(s)-1} \mbox{Seed}^i * \mbox{charvalue}(s[i])\right) \mbox{ mod } \mbox{NumBuckets}.
# $$
# 
# The "InitialValue" and "Seed" are parameters. The function "charvalue`(c)`" converts a single letter into a number. Finally, "NumBuckets" is the number of buckets.
# 
# For example, consider the input string, `s="midterm"` and suppose there are 10 buckets (NumBuckets=10). Suppose that InitialValue is 37 and Seed is 7. Further suppose that for the letter `a`, charvalue(`'a'`) is 97, and that the subsequent letters are numbered consecutively, i.e., so `b` is 98, ..., `d`=100, ..., `i`=105, `m` = 109, ...). Then HashFunction(`"midterm"`) is
# 
# $$
# (37+7^0*109+7^1*105+7^2*100+7^3*116+7^4*101+7^5*114+7^6*109) \mbox{ mod } 10 = (15,027,809 \mbox{ mod } 10) = 9.
# $$

# We will give you a `seed` value and an `initial value`. Create a function that implements the formula for HashFunction(`s`), given the string `s` and number of buckets `num_buckets`, returning the bucket ID.
# 
# > Recall that the `a % b` operator implements `a` modulo `b`. To convert an individual letter to an integer (i.e., to implement charvalue(c)), use Python's [`ord`](https://docs.python.org/3/library/functions.html#ord) function.

# In[3]:


SEED = 7
INITIALVALUE = 37


# In[4]:


def hash_function(s, num_buckets):
    assert num_buckets > 0.0
    ords = []
    
    for i in s:
        ords.append(ord(i))
        
    hash_start = []
    
    
    for index, value in enumerate(ords):
        if index < len(ords):
            hash_start.append(value * (SEED**(index)))
        else:
            hash_start.append(float(value))
                             
    hash_sum = sum(hash_start)

        
    hash_complete = (hash_sum + INITIALVALUE) % num_buckets
        
    
    return hash_complete

hash_function('midterm', 10)
hash_function("jack", 20)


# In[5]:


#test_hash (2 points):
assert type(hash_function('midterm', 10)) is int
assert hash_function('midterm', 10) == 9
assert hash_function('problems', 12) == 5
assert hash_function('problem', 1) == 0
print ("\n(Passed!)")


# **Collisions.** Collisions occur when two keys have the same bucket ID. There are many methods to deal with collisions, but you will implement a method known as _separate chaining_.
# 
# In separate chaining, each bucket is a list, again implemented as a Python `list`. That way, it can hold multiple items of the same hash value. When adding a new item to the hash table, you can simply append that item onto the bucket.
# 
# In other words, the overall hash table is a list of lists: a list of buckets, where each bucket is also a list (of items).
# 
# Here is a helpful graphic displaying this concept. Focus on the `keys` for `John Smith` and `Sandra Dee`, supposing that their hash values collide:
# 
# ![](https://upload.wikimedia.org/wikipedia/commons/d/d0/Hash_table_5_0_1_1_1_1_1_LL.svg "Separate Chaining")
# 

# ** Exercise 1 (3 points)**: Create the `hash_insert()` function for your hash table. This function will take in three arguments. The first is the string `key`, the second is the string `value`, and the third is the `buckets`, a Python `list` that represents the hash table buckets. Your function should add the given `(key, value)` tuple to the list, implementing the separate chaining logic if there is a collision.
# 
# And if an identical `key` already exists in the hash table, your function should replace the current value with this new `value`.
# 
# A reasonable algorithm for this problem would be the following:
# 
# 1. Compute the bucket ID for the given `key`.
# 2. If the bucket is empty, append (`key`, `value`) to that bucket.
# 3. If the bucket is not empty, then there are two cases:
#     a. If `key` is already in the bucket, then update the old value with the given `value`.
#     b. If `key` is not yet in the bucket, then simply append (`key`, `value`) to the bucket.
# 
# You may assume that every element of `buckets` is a valid `list` object. (It might be empty, but it will be a list.)

# In[6]:


def hash_insert(key, value, buckets): 
    assert len(buckets) > 0
    assert all([type(b) is list for b in buckets])
    
    ### BEGIN SOLUTION
    hash_value = hash_function(key, len(buckets))
    bucket = buckets[hash_value]
    if len(bucket):
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, value)
                return
    bucket.append((key, value))




# In[7]:


#test_add (3 points):
table = [[] for i in range(20)]
hash_insert("jack", "8048148198", table)
hash_insert("asdf1", "8048148198", table)
assert type(table[14]) is list
assert len(table[14]) == 2
hash_insert("asdf2", "8048148198", table)
hash_insert("asdf3", "8048148198", table)
assert len(table[15]) == 1
assert len(table[16]) == 1
print ("\n(Passed!)")


# ** Exercise 2 (2 points)**. Implement a search operation, `hash_search()`. This operation would be used to implement Python's `dict[key]`.
# 
# Your function should implement the following logic. Given a `key` and `buckets`, return the `value` associated with that `key`. If the key does not exist, return `None`.

# In[10]:


def hash_search(key, buckets):
    assert len(buckets) > 0 and all([type(b) is list for b in buckets])
    
    ### BEGIN SOLUTION
    bucket = buckets[hash_function(key, len(buckets))]
    for (k, v) in bucket:
        if k == key:
            return v


# In[11]:


#test_cell
assert(hash_search("evan", table)) is None
assert hash_search("asdf1", table) == '8048148198'
print ("\n(Passed!)")


# **Putting it all together.** You will be supplied with a dataset of 1,000 name and phone number pairs, contained in a list-of-lists named `hash_table_data`. The following code cell will read in these data.

# In[12]:


import csv
hash_table_data = list()
with open("name_phonenumber_map.csv", "r") as f:
    reader = csv.reader(f)
    for line in f:
        hash_table_data.append(line.replace("\r\n", "").split(","))
        
print("First few entries: {} ...".format(hash_table_data[:5]))


#  **Exercise 3 (3 points)**: Use your functions from the first three exercises to create a hash table from the above dataset, `hash_table_data`. Store this table in a variable named `table`.
#  
# In other words, iterate through `hash_table_data` and insert each `(name, phone number)` pair into your `table`. 
# 
# You will have to choose a specific size for your `table`. In practice, the size is often chosen to try to achieve a certain *load factor," which is defined as
# 
# $$
# \mbox{load factor} \equiv \frac{n}{k},
# $$
# 
# where $n$ is the number of items (i.e., key-value pairs) you expect to store and $k$ is the number of buckets. Common *load factor* values are 0.5 or 0.75. Remember that there are 1,000 entries in the `hash_table_data` dataset, so choose your number of buckets accordingly.
# 
# You will be graded in two ways. The first test cell, worth one point, will test a correct import of the data into your `table`. The next test cell will test how your `hash_insert()` and `hash_search()` functions work with your newly created `table`. 

# In[13]:


num_buckets = 2 * len(hash_table_data) # Based on a load factor of 0.5
table = [[] for i in range(num_buckets)]
for l in hash_table_data:
    hash_insert(l[0], l[1], table)


# In[15]:


# test_cell_1 (1 point)
assert type(table) is list
for i in range(0,len(hash_table_data)):
    assert hash_search(hash_table_data[i][0], table) is not None
print ("\n(Passed!)")


# In[16]:


#test_cell_2 (2 points)
assert (hash_search('Harriott Loan', table) == [s for s in hash_table_data if "Harriott Loan" in s ][0][1])
print ("\n(Passed!)")


# ** Fin ** You've reached the end of this problem. Don't forget to restart the
# kernel and run the entire notebook from top-to-bottom to make sure you did
# everything correctly. If that is working, try submitting this problem. (Recall
# that you *must* submit and pass the autograder to get credit for your work.)
