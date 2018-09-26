
# coding: utf-8

# # Problem 2: DNA Sequence Analysis
# 
# This problem is about strings and regular expressions. It has four (4) exercises, numbered 0-3. They are worth a total of ten (10) points.

# In[1]:


import re # You'll need this module


# ## DNA Sequence Analysis
# 
# Your friend is a biologist who is studying a particular DNA sequence. The sequence is a string built from an alphabet of four possible letters, `A`, `G`, `C`, and `T`. Biologists refer to each of these letters a _base_.
# 
# Here is an example of a DNA fragment as a string of bases.

# In[2]:


dna_seq = 'ATGGCAATAACCCCCCGTTTCTACTTCTAGAGGAGAAAAGTATTGACATGAGCGCTCCCGGCACAAGGGCCAAAGAAGTCTCCAATTTCTTATTTCCGAATGACATGCGTCTCCTTGCGGGTAAATCACCGACCGCAATTCATAGAAGCCTGGGGGAACAGATAGGTCTAATTAGCTTAAGAGAGTAAATCCTGGGATCATTCAGTAGTAACCATAAACTTACGCTGGGGCTTCTTCGGCGGATTTTTACAGTTACCAACCAGGAGATTTGAAGTAAATCAGTTGAGGATTTAGCCGCGCTATCCGGTAATCTCCAAATTAAAACATACCGTTCCATGAAGGCTAGAATTACTTACCGGCCTTTTCCATGCCTGCGCTATACCCCCCCACTCTCCCGCTTATCCGTCCGAGCGGAGGCAGTGCGATCCTCCGTTAAGATATTCTTACGTGTGACGTAGCTATGTATTTTGCAGAGCTGGCGAACGCGTTGAACACTTCACAGATGGTAGGGATTCGGGTAAAGGGCGTATAATTGGGGACTAACATAGGCGTAGACTACGATGGCGCCAACTCAATCGCAGCTCGAGCGCCCTGAATAACGTACTCATCTCAACTCATTCTCGGCAATCTACCGAGCGACTCGATTATCAACGGCTGTCTAGCAGTTCTAATCTTTTGCCAGCATCGTAATAGCCTCCAAGAGATTGATGATAGCTATCGGCACAGAACTGAGACGGCGCCGATGGATAGCGGACTTTCGGTCAACCACAATTCCCCACGGGACAGGTCCTGCGGTGCGCATCACTCTGAATGTACAAGCAACCCAAGTGGGCCGAGCCTGGACTCAGCTGGTTCCTGCGTGAGCTCGAGACTCGGGATGACAGCTCTTTAAACATAGAGCGGGGGCGTCGAACGGTCGAGAAAGTCATAGTACCTCGGGTACCAACTTACTCAGGTTATTGCTTGAAGCTGTACTATTTTAGGGGGGGAGCGCTGAAGGTCTCTTCTTCTCATGACTGAACTCGCGAGGGTCGTGAAGTCGGTTCCTTCAATGGTTAAAAAACAAAGGCTTACTGTGCGCAGAGGAACGCCCATCTAGCGGCTGGCGTCTTGAATGCTCGGTCCCCTTTGTCATTCCGGATTAATCCATTTCCCTCATTCACGAGCTTGCGAAGTCTACATTGGTATATGAATGCGACCTAGAAGAGGGCGCTTAAAATTGGCAGTGGTTGATGCTCTAAACTCCATTTGGTTTACTCGTGCATCACCGCGATAGGCTGACAAAGGTTTAACATTGAATAGCAAGGCACTTCCGGTCTCAATGAACGGCCGGGAAAGGTACGCGCGCGGTATGGGAGGATCAAGGGGCCAATAGAGAGGCTCCTCTCTCACTCGCTAGGAGGCAAATGTAAAACAATGGTTACTGCATCGATACATAAAACATGTCCATCGGTTGCCCAAAGTGTTAAGTGTCTATCACCCCTAGGGCCGTTTCCCGCATATAAACGCCAGGTTGTATCCGCATTTGATGCTACCGTGGATGAGTCTGCGTCGAGCGCGCCGCACGAATGTTGCAATGTATTGCATGAGTAGGGTTGACTAAGAGCCGTTAGATGCGTCGCTGTACTAATAGTTGTCGACAGACCGTCGAGATTAGAAAATGGTACCAGCATTTTCGGAGGTTCTCTAACTAGTATGGATTGCGGTGTCTTCACTGTGCTGCGGCTACCCATCGCCTGAAATCCAGCTGGTGTCAAGCCATCCCCTCTCCGGGACGCCGCATGTAGTGAAACATATACGTTGCACGGGTTCACCGCGGTCCGTTCTGAGTCGACCAAGGACACAATCGAGCTCCGATCCGTACCCTCGACAAACTTGTACCCGACCCCCGGAGCTTGCCAGCTCCTCGGGTATCATGGAGCCTGTGGTTCATCGCGTCCGATATCAAACTTCGTCATGATAAAGTCCCCCCCTCGGGAGTACCAGAGAAGATGACTACTGAGTTGTGCGAT'
print("=== Sequence (Number of bases: {}) ===\n\n{}".format(len(dna_seq), dna_seq))


# In this problem, you will help your friend analyze this sequence.

# **Exercise 0** (2 point). Complete the function, `count_bases(s)`. It takes as input a DNA sequence as a string, `s`. It should compute the number of occurrences of each base (i.e., `'A'`, `'C'`, `'G'`, and `'T'`) in `s`. It should then return these counts in a dictionary whose keys are the bases.

# In[6]:


from collections import defaultdict


def count_bases(s):
    bases_dict = defaultdict(int)
    assert type(s) is str
    assert all([b in ['A', 'C', 'G', 'T'] for b in s])
    patternA = re.findall(r'A', s)
    patternC = re.findall(r'C', s)
    patternG = re.findall(r'G', s)
    patternT = re.findall(r'T', s)
    
    bases_dict['A'] = len(patternA)
    bases_dict['C'] = len(patternC)
    bases_dict['G'] = len(patternG)
    bases_dict['T'] = len(patternT)
    
    return dict(bases_dict)

count_bases(dna_seq)
        
    
    


# In[7]:


# Test cell: `exercise_0_test`

base_counts = count_bases(dna_seq)
print("Your result:", base_counts)

assert type(base_counts) is dict, "`base_counts` is of type `{}`, not `dict`.".format(type(base_counts))
assert len(base_counts) <= 4, "There can be at most 4 bases."
for b, c in [('A', 501), ('C', 507), ('G', 508), ('T', 496)]:
    assert base_counts[b] == c, "Base '{}' has a count of {} when it should be {}.".format(b, base_counts[b], c)
    
print("\n(Passed!)")


# **Enzyme "scissors."** Your friend is interested in what will happen to the sequence if she uses certain "restriction enzymes" to cut it. The enzymes work by scanning the DNA sequence from left to right for a particular pattern. It then cuts the DNA wherever it finds a match.

# **A biologist's notation.** Your friend does not know about regular expressions. Instead, she uses a [special notation](https://en.wikipedia.org/wiki/Nucleic_acid_sequence) that other biologists use to describe base patterns. These are "extra letters" that have a special meaning.
# 
# For example, the special letter `N` denotes any base, i.e., any single occurrence of an `A`, `C`, `G`, or `T`. Therefore, when a biologist writes, `ANT`, that means `AAT`, `ACT`, `AGT`, or `ATT`.
# 
# Here is the complete set of special letters:
# 
# * `R`: Either `G` or `A`
# * `Y`: Either `T` or `C`
# * `K`: Either `G` or `T`
# * `M`: Either `A` or `C`
# * `S`: Either `G` or `C`
# * `W`: Either `A` or `T`
# * `B`: Anything but `A` (i.e., `G`, `T`, or `C`)
# * `D`: Anything but `C`
# * `H`: Anything but `G`
# * `V`: Anything but `T`
# * `N`: Anything, i.e., `A`, `C`, `G`, or `T`

# **Exercise 1** (4 points). Given a string in the biologist's notation, complete the function `bio_to_regex(pattern_bio)` so that it returns an equivalent pattern in Python's regular expression language.
# 
# If your function is correct, then the following code would also work:
# 
# ```python
#   assert re.search(bio_to_regex('ANT'), 'AGATTA') is not None
# ```
# 
# That's because `ANT` matches `ATT`, which is contained in `AGATTA`.

# In[36]:


def bio_to_regex(pattern_bio):
    ### BEGIN SOLUTION
    # A handy conversion table, to map bio letters to regex subpatterns:
    translation_table = {'R': '[AG]', 'Y': '[TC]', 'K': '[GT]', 'M': '[AC]', 'S': '[GC]', 'W': '[AT]',
                         'B': '[^A]', 'D': '[^C]', 'H': '[^G]', 'V': '[^T]', 'N': '.'}
    
    # Here is the most compact solution we came up with:
    translator = str.maketrans(translation_table)
    return pattern_bio.translate(translator)





        


# In[37]:


# Test cell: `exercise_1_test_0`

assert re.search(bio_to_regex('ANT'), 'AGATTA') is not None
assert set(re.findall(bio_to_regex('ANTAAT'), dna_seq)) == {'ATTAAT', 'ACTAAT'}
assert set(re.findall(bio_to_regex('GCRWTG'), dna_seq)) == {'GCGTTG', 'GCAATG'}
assert len(re.findall(bio_to_regex('CDCHA'), dna_seq)) == 18

print("\n(Passed first group of tests!)")


# In[38]:


# Test cell: `exercise_1_test_1`
if False:
    for c in {'Y', 'K', 'M', 'S', 'B', 'D', 'V'}:
        from random import sample
        x = ''.join([sample('ACGT', 1)[0] for _ in range(2)])
        y = ''.join([sample('ACGT', 1)[0] for _ in range(2)])
        pattern = '{}{}{}'.format(x, c, y)
        ans = set(re.findall(bio_to_regex(pattern), dna_seq))
        print("assert set(re.findall(bio_to_regex('{}'), dna_seq)) == {}".format(pattern, ans))
        
assert set(re.findall(bio_to_regex('GABAT'), dna_seq)) == {'GACAT', 'GAGAT', 'GATAT'}
assert set(re.findall(bio_to_regex('GAVCA'), dna_seq)) == {'GACCA', 'GAACA'}
assert set(re.findall(bio_to_regex('TGYGG'), dna_seq)) == {'TGTGG', 'TGCGG'}
assert set(re.findall(bio_to_regex('GCKAA'), dna_seq)) == {'GCGAA'}
assert set(re.findall(bio_to_regex('ATSCA'), dna_seq)) == {'ATCCA'}
assert set(re.findall(bio_to_regex('GCMTT'), dna_seq)) == {'GCCTT', 'GCATT'}
assert set(re.findall(bio_to_regex('AGDCC'), dna_seq)) == {'AGTCC', 'AGACC'}

print("\n(Passed second set of tests!)")


# **Restriction sites.** When an enzyme cuts the string, it does it in a certain location with respect to the target pattern. This information is encoded as a _restriction site_.
# 
# The way a biologist specifies the restriction site is with a special notation that embeds the cut in the pattern. For example, there is one enzyme that has a restriction site of the form, `ANT|AAT`, where the vertical bar, `'|'`, shows where the enzyme will split the sequence. So, if the input DNA sequence were
# 
# ```
#    GCATAGTAATGTATTAATGGC
# ```
# 
# then there would two matches:
# 
# ```
#    GCATAGTAATGTATTAATGGC
#        ^^^^^^  ^^^^^^
#        match!  match!
# ```
# 
# Furthermore, there would be two cuts, since this enzyme splits its pattern in the middle (between `ANT` and `AAT`):
# 
# ```
#    GCATAGT|AATGTATT|AATGGC
#        ^^^ ^^^  ^^^ ^^^
# ```
# 
# That would result in three fragments: `GCATAGT`, `AATGTATT`, and `AATGGC`.

# **Exercise 3** (5 points). Complete the function, `sim_cuts(site_pattern, s)`, below. The first argument, `site_pattern`, is the biologist's restriction site pattern, e.g., `ANT|AAT`, where there may be an embedded cut. The second argument, `s`, is the DNA sequence to cut. The function should return the fragments in the sequence order.
# 
# For the preceding example,
# 
# ```python
#   sim_cuts('ANT|AAT', 'GCATAGTAATGTATTAATGGC') == ['GCATAGT', 'AATGTATT', 'AATGGC']
# ```
# 
# > **Note.** There are *two* test cells, below. Both must pass for full credit, but if only one passes, you'll at least get some partial credit.

# In[39]:


def sim_cuts(site_pattern, s):
    ### BEGIN SOLUTION
    cut_parts = site_pattern.split('|')
    pure_bio_parts = ['(' + p + ')' for p in cut_parts]
    pure_bio_pattern = ''.join(pure_bio_parts)
    regex_pattern = bio_to_regex(pure_bio_pattern)
    repl_parts = [r'\{}'.format(i+1) for i in range(len(cut_parts))]
    repl_pattern = '|'.join(repl_parts)
    s_with_cuts = re.sub(regex_pattern, repl_pattern, s)
    return s_with_cuts.split('|')


# In[40]:


# Test cell: `exercise_3_test_0`

def check_sim_cuts(bio_pattern, s, true_cuts):
    print("\nChecking: '{}'...".format(bio_pattern))
    your_cuts = sim_cuts(bio_pattern, s)
    print("   Your result ({} fragments): {}".format(len(your_cuts), your_cuts))
    print("   True result ({}): {}".format(len(true_cuts), true_cuts))
    assert your_cuts == true_cuts, "Did not match!"
    print("   ==> Matched!")

# Check a simple case:
check_sim_cuts('ANT|AAT', 'GCATAGTAATGTATTAATGGC', ['GCATAGT', 'AATGTATT', 'AATGGC'])

print("\n(Passed first test of Exercise 3; two more to go in the next cell.)")


# In[41]:


# Test cell: `exercise_2_test_1`

check_sim_cuts('ANT|AAT', dna_seq, ['ATGGCAATAACCCCCCGTTTCTACTTCTAGAGGAGAAAAGTATTGACATGAGCGCTCCCGGCACAAGGGCCAAAGAAGTCTCCAATTTCTTATTTCCGAATGACATGCGTCTCCTTGCGGGTAAATCACCGACCGCAATTCATAGAAGCCTGGGGGAACAGATAGGTCTAATTAGCTTAAGAGAGTAAATCCTGGGATCATTCAGTAGTAACCATAAACTTACGCTGGGGCTTCTTCGGCGGATTTTTACAGTTACCAACCAGGAGATTTGAAGTAAATCAGTTGAGGATTTAGCCGCGCTATCCGGTAATCTCCAAATTAAAACATACCGTTCCATGAAGGCTAGAATTACTTACCGGCCTTTTCCATGCCTGCGCTATACCCCCCCACTCTCCCGCTTATCCGTCCGAGCGGAGGCAGTGCGATCCTCCGTTAAGATATTCTTACGTGTGACGTAGCTATGTATTTTGCAGAGCTGGCGAACGCGTTGAACACTTCACAGATGGTAGGGATTCGGGTAAAGGGCGTATAATTGGGGACTAACATAGGCGTAGACTACGATGGCGCCAACTCAATCGCAGCTCGAGCGCCCTGAATAACGTACTCATCTCAACTCATTCTCGGCAATCTACCGAGCGACTCGATTATCAACGGCTGTCTAGCAGTTCTAATCTTTTGCCAGCATCGTAATAGCCTCCAAGAGATTGATGATAGCTATCGGCACAGAACTGAGACGGCGCCGATGGATAGCGGACTTTCGGTCAACCACAATTCCCCACGGGACAGGTCCTGCGGTGCGCATCACTCTGAATGTACAAGCAACCCAAGTGGGCCGAGCCTGGACTCAGCTGGTTCCTGCGTGAGCTCGAGACTCGGGATGACAGCTCTTTAAACATAGAGCGGGGGCGTCGAACGGTCGAGAAAGTCATAGTACCTCGGGTACCAACTTACTCAGGTTATTGCTTGAAGCTGTACTATTTTAGGGGGGGAGCGCTGAAGGTCTCTTCTTCTCATGACTGAACTCGCGAGGGTCGTGAAGTCGGTTCCTTCAATGGTTAAAAAACAAAGGCTTACTGTGCGCAGAGGAACGCCCATCTAGCGGCTGGCGTCTTGAATGCTCGGTCCCCTTTGTCATTCCGGATT',
 'AATCCATTTCCCTCATTCACGAGCTTGCGAAGTCTACATTGGTATATGAATGCGACCTAGAAGAGGGCGCTTAAAATTGGCAGTGGTTGATGCTCTAAACTCCATTTGGTTTACTCGTGCATCACCGCGATAGGCTGACAAAGGTTTAACATTGAATAGCAAGGCACTTCCGGTCTCAATGAACGGCCGGGAAAGGTACGCGCGCGGTATGGGAGGATCAAGGGGCCAATAGAGAGGCTCCTCTCTCACTCGCTAGGAGGCAAATGTAAAACAATGGTTACTGCATCGATACATAAAACATGTCCATCGGTTGCCCAAAGTGTTAAGTGTCTATCACCCCTAGGGCCGTTTCCCGCATATAAACGCCAGGTTGTATCCGCATTTGATGCTACCGTGGATGAGTCTGCGTCGAGCGCGCCGCACGAATGTTGCAATGTATTGCATGAGTAGGGTTGACTAAGAGCCGTTAGATGCGTCGCTGTACT',
 'AATAGTTGTCGACAGACCGTCGAGATTAGAAAATGGTACCAGCATTTTCGGAGGTTCTCTAACTAGTATGGATTGCGGTGTCTTCACTGTGCTGCGGCTACCCATCGCCTGAAATCCAGCTGGTGTCAAGCCATCCCCTCTCCGGGACGCCGCATGTAGTGAAACATATACGTTGCACGGGTTCACCGCGGTCCGTTCTGAGTCGACCAAGGACACAATCGAGCTCCGATCCGTACCCTCGACAAACTTGTACCCGACCCCCGGAGCTTGCCAGCTCCTCGGGTATCATGGAGCCTGTGGTTCATCGCGTCCGATATCAAACTTCGTCATGATAAAGTCCCCCCCTCGGGAGTACCAGAGAAGATGACTACTGAGTTGTGCGAT'])
check_sim_cuts('GCRW|TG', dna_seq, ['ATGGCAATAACCCCCCGTTTCTACTTCTAGAGGAGAAAAGTATTGACATGAGCGCTCCCGGCACAAGGGCCAAAGAAGTCTCCAATTTCTTATTTCCGAATGACATGCGTCTCCTTGCGGGTAAATCACCGACCGCAATTCATAGAAGCCTGGGGGAACAGATAGGTCTAATTAGCTTAAGAGAGTAAATCCTGGGATCATTCAGTAGTAACCATAAACTTACGCTGGGGCTTCTTCGGCGGATTTTTACAGTTACCAACCAGGAGATTTGAAGTAAATCAGTTGAGGATTTAGCCGCGCTATCCGGTAATCTCCAAATTAAAACATACCGTTCCATGAAGGCTAGAATTACTTACCGGCCTTTTCCATGCCTGCGCTATACCCCCCCACTCTCCCGCTTATCCGTCCGAGCGGAGGCAGTGCGATCCTCCGTTAAGATATTCTTACGTGTGACGTAGCTATGTATTTTGCAGAGCTGGCGAACGCGT',
 'TGAACACTTCACAGATGGTAGGGATTCGGGTAAAGGGCGTATAATTGGGGACTAACATAGGCGTAGACTACGATGGCGCCAACTCAATCGCAGCTCGAGCGCCCTGAATAACGTACTCATCTCAACTCATTCTCGGCAATCTACCGAGCGACTCGATTATCAACGGCTGTCTAGCAGTTCTAATCTTTTGCCAGCATCGTAATAGCCTCCAAGAGATTGATGATAGCTATCGGCACAGAACTGAGACGGCGCCGATGGATAGCGGACTTTCGGTCAACCACAATTCCCCACGGGACAGGTCCTGCGGTGCGCATCACTCTGAATGTACAAGCAACCCAAGTGGGCCGAGCCTGGACTCAGCTGGTTCCTGCGTGAGCTCGAGACTCGGGATGACAGCTCTTTAAACATAGAGCGGGGGCGTCGAACGGTCGAGAAAGTCATAGTACCTCGGGTACCAACTTACTCAGGTTATTGCTTGAAGCTGTACTATTTTAGGGGGGGAGCGCTGAAGGTCTCTTCTTCTCATGACTGAACTCGCGAGGGTCGTGAAGTCGGTTCCTTCAATGGTTAAAAAACAAAGGCTTACTGTGCGCAGAGGAACGCCCATCTAGCGGCTGGCGTCTTGAATGCTCGGTCCCCTTTGTCATTCCGGATTAATCCATTTCCCTCATTCACGAGCTTGCGAAGTCTACATTGGTATATGAATGCGACCTAGAAGAGGGCGCTTAAAATTGGCAGTGGTTGATGCTCTAAACTCCATTTGGTTTACTCGTGCATCACCGCGATAGGCTGACAAAGGTTTAACATTGAATAGCAAGGCACTTCCGGTCTCAATGAACGGCCGGGAAAGGTACGCGCGCGGTATGGGAGGATCAAGGGGCCAATAGAGAGGCTCCTCTCTCACTCGCTAGGAGGCAAATGTAAAACAATGGTTACTGCATCGATACATAAAACATGTCCATCGGTTGCCCAAAGTGTTAAGTGTCTATCACCCCTAGGGCCGTTTCCCGCATATAAACGCCAGGTTGTATCCGCATTTGATGCTACCGTGGATGAGTCTGCGTCGAGCGCGCCGCACGAATGTTGCAA',
 'TGTATTGCATGAGTAGGGTTGACTAAGAGCCGTTAGATGCGTCGCTGTACTAATAGTTGTCGACAGACCGTCGAGATTAGAAAATGGTACCAGCATTTTCGGAGGTTCTCTAACTAGTATGGATTGCGGTGTCTTCACTGTGCTGCGGCTACCCATCGCCTGAAATCCAGCTGGTGTCAAGCCATCCCCTCTCCGGGACGCCGCATGTAGTGAAACATATACGTTGCACGGGTTCACCGCGGTCCGTTCTGAGTCGACCAAGGACACAATCGAGCTCCGATCCGTACCCTCGACAAACTTGTACCCGACCCCCGGAGCTTGCCAGCTCCTCGGGTATCATGGAGCCTGTGGTTCATCGCGTCCGATATCAAACTTCGTCATGATAAAGTCCCCCCCTCGGGAGTACCAGAGAAGATGACTACTGAGTTGTGCGAT'])

print("\n(Passed second tests of Exercise 3!)")


# **Fin!** If you've reached this point and all tests above pass, your biologist friend thanks you and you are ready to submit your solution to this problem. Don't forget to save you work prior to submitting.
# 
# Portions of this problem were inspired by a fun book called [Python for Biologists](https://pythonforbiologists.com/python-books).

# In[42]:


print("\n(This notebook ran to completion.)")

