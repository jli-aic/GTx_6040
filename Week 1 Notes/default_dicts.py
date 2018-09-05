# coding our association rules algorithm into python notes

'''
our algorithm essentially manipulates our tables T and C with counts
how do we store these tables?
we do not want to store all of the pairs if we don't have to (keeps Table T lean)
we want our table to be sparse (many entries will be 0 and not need to be stored)
dictionary is a great way to store this data:
- the key will be a pair of letters
- the value will be the count of this pair
- we will only create an entry if there is at least one item pair
- otherwise we can assume that a missing entry is implicitly 0
- this is a clever way to expliot sparsity!
'''

'''
defaultDictionary: updating values for an existing key
if key does not already exist we will throw an error trying to update dictionaries
this means we must always write a code that checks for the available key first
'''

D = {'existing_key': 5} # dictionary with one key-value pair

D['existing_key'] += 1 # will increment D to existing_key == 6
D['key_key'] += 1 # error: key does not exist


'''
The second attempt causes an error because 'new-key' is not yet a member of the
dictionary. So, a more correct approach would be to do the following:
'''

D = {'existing-key': 5} # Dictionary with one key-value pair

if 'existing-key' not in D:
    D['existing-key'] = 0
D['existing-key'] += 1

if 'new-key' not in D:
    D['new-key'] = 0
D['new-key'] += 1



'''
defaultDictionary hides the check!
we need to supply a 'factory function' to build the base dictionary
'''

from collections import defaultdict

D2 = defaultdict (int) # Empty dictionary

D2['existing-key'] = 5 # Create one key-value pair

D2['existing-key'] += 1 # Update
D2['new-key'] += 1

print (D2)
