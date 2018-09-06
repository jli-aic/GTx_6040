
# coding: utf-8

# # Problem 8
# 
# This problem has three (3) exercises worth a total of ten (10) points.

# **Invert a dictionary.** Suppose a group of student TAs have been asked to monitor the Piazza forums for your CSE6040x course. The assignments are as follows.

# In[20]:


assignments = {"Monday" : ["Jeh", "Ben", "Chinmay", "Rachel"],
               "Tuesday" : ["Rachel", "Samuel", "Evan", "Raghav"],
               "Wednesday" : ["Evan", "Samuel", "Michael", "Chinmay"],
               "Thursday" : ["Jeh", "Michael", "Ben", "Evan"],
               "Friday" : ["Rachel", "Shishir", "Samuel", "Ben"],
               "Saturday" : ["Yandi", "Michael", "Chinmay", "Samuel"],
               "Sunday" : ["Evan", "Chinmay", "Jeh", "Rachel"]
               }


# **Exercise 0** (5 points). Write a function, `invert_dict(d)`, that "inverts" a given dictionary `d`. The output should be another dictionary such that the keys are the TA names and their corresponding values should be a list which stores the days assigned to them.
# 
# For example, one of the keys of the returned dictionary should be `"Jeh"` with its corresponding list as `["Monday", "Thursday", "Sunday"]`.

# In[21]:


from collections import defaultdict

def invert_dict(d):
    l = []
    for k, v in d.items():
        l.append(v)
    flatten_l = [i for e in l for i in e]
    flatten_l = set(flatten_l)
    d_inv = defaultdict(list)
    for e in flatten_l:
        for k, v in d.items():
            if e in v:
                d_inv[e].append(k)
    return dict(d_inv)

invert_dict(assignments)


# In[22]:


# Test cell: `test_inverse`

import random
TA_list = ["Rachel", "Yandi", "Ben", "Jeh", "Evan", "Chinmay", "Shishir", "Raghav", "Samuel", "Michael"]

# Your solution
inv_dict = invert_dict(assignments)

random_TA = random.sample(TA_list, 5)
for TA in random_TA:
    assigned_days = inv_dict[TA]
    for days in assigned_days:
        assert TA in assignments[days], "Incorrect inversion for TA {}".format(TA)

print("\n(Passed!)")


# **Exercise 2** (2 points): _Tracing the route of a pilot_.
# 
# Suppose a pilot flies from one city to the next. He makes 7 such trips, which are stored in the list shown in the next cell. The first entry of each tuple denotes the origin, and the second denotes the destination. Also assume that the next flight a pilot makes must originate from the destination of her previous flight. Your task in this exercise is to write a function that finds the route followed by the pilot, given her first port of origin.
# 
# First, let `segments` be an unordered list of segments that the pilot flew.

# In[23]:


segments = [("JFK", "DEN"), ("LAX", "ORD"), ("DEN", "SFO"), ("LAS", "LAX"), ("ORD", "ATL"), ("ATL", "JFK"), ("SFO", "LAS")]


# Next, write a function `find_dest(segs, origin)` that returns the next destination of the pilot given one port of origin and an unordered list of flight segments. Example, if `segs == segments` as defined above, then for `'LAX'`, your function should return `'ORD'` because there is the tuple, `("LAX", "ORD")`, in `segs`.
# 
# You may assume that `origin` appears only once in the list of segments, `segs`.

# In[27]:


def find_dest(segs, origin):
    assert type(origin) is str
    assert type(segs) is list
    for i in segs:
        if i[0] == origin:
            dest = i[1]
    return dest

find_dest(segments, "DEN")


# In[26]:


# Test flight destination
den = find_dest(segments, "DEN")
assert find_dest(segments, "DEN") == "SFO", "Wrong destination for DEN"
assert find_dest(segments, "LAX") == "ORD", "Wrong destination for LAX"
assert find_dest(segments, "ATL") == "JFK", "Wrong destination for ATL"
assert find_dest(segments, "JFK") == "DEN", "Wrong destination for JFK"
print("\n(Passed.)")


# **Exercise 3** (3 points). Now write a function `get_route(segs, origin)` that traces the complete itinerary of the pilot, given her first port of origin. Assume that the destination for a flight is the same as the origin for the next flight. The itinerary is completed when he arrives back at the starting port of origin. For example, if the starting port is `"JFK"`, your function should return the list: `["JFK", "DEN", "SFO", "LAS", "LAX", "ORD", "ATL"]`.

# In[32]:


def get_route(path, origin):
    route = [origin]
    dest = find_dest(path, origin)
    while dest != origin:
        route.append(dest)
        dest = find_dest(path, dest)
    return route

get_route(segments, "DEN")


# In[33]:


# Test pilot route
ports = ["JFK", "DEN", "SFO", "LAS", "LAX", "ORD", "ATL"]
starting_port = random.sample(ports, 5)
for p in starting_port:
    itinerary = get_route(segments, p)
    assert itinerary[0] == p, "incorrect port of origin for the itinerary"
    for i, port in enumerate(itinerary[:-1]):
        dest = find_dest(segments, port)
        assert dest == itinerary[i+1], "incorrect itinerary"

print("\n(Passed.)")


# **Fin!** You've reached the end of this problem. Don't forget to restart the
# kernel and run the entire notebook from top-to-bottom to make sure you did
# everything correctly. If that is working, try submitting this problem. (Recall
# that you *must* submit and pass the autograder to get credit for your work!)
