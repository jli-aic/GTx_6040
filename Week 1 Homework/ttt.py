
# coding: utf-8

# ## Problem 10: Tic-Tac-Toe!
# 
# The objective of this exercise is to check whether you can declare a winner based on the current state of a Tic-Tac-Toe (TTT) game (https://en.wikipedia.org/wiki/Tic-tac-toe).
# 
# A state in the game of TTT can be represented as a list of lists as follows
# 
# 1. Crosses are represented by -1
# 2. Circles are represented by +1
# 3. Unused cells are represented by 0
# 
# For example, the game below
# 
# ||col0|col1|col2|
# |-|-|-|--|
# |row0|0|0|-1|
# |row1|1|-1|1|
# |row2|-1|1|0|
# 
# can be represented as a list of lists
# ```python
# [[0,0,-1],
#  [1,-1,1],
#  [-1,1,0]]
# ```

# **Exercise 0**  Write a function called `check_ttt(game)` that takes a list of 3 lists representing each row of a game's state and determines whether or not there is a winner. In particular, it should return one of the following strings:
# 
# 1. `"Circles (+1) Win"`
# 2. `"Crosses (-1) Win"`
# 3. `"No Result"`
# 
# For example,
# 
# ```python
#     assert check_ttt([[0,0,-1],[1,-1,1],[-1,1,0]]) == "Crosses (-1) Win"
# ```
# 
# since there are three crosses (-1 values) along one of the diagonals of this board state.
# 
# You may assume that the input is a valid game state, i.e., a list representing a $3 \times 3$ grid with all cells having integer values in $\{-1,0,1\}$ and at most one current winner.

# In[13]:


def check_ttt(game):
    # Check that the input is valid
    assert type(game) == list
    assert all([type(row) == list for row in game])
    assert all([[elem in [0,1,-1] for elem in row] for row in game])
    
    # check for horizontal and vertical wins
    for num in range(3):
        h_sum = sum(game[num])
        v_sum = sum([v[num] for v in game])
        if max(h_sum, v_sum) == 3:
            return 'Circles (+1) Win'
        elif min(h_sum, v_sum) == -3:
            return 'Crosses (-1) Win'
        
    # check for diagonal wins
    diag_for = sum([diag[i] for i, diag in enumerate(game)])
    diag_back = sum([diag[2-i] for i, diag in enumerate(game)])
    if max(diag_for, diag_back) == 3:
        return 'Circles (+1) Win'
    elif min(diag_for, diag_back) == -3:
        return 'Crosses (-1) Win'
            
        
    return 'No Result'




# In[15]:


# Test cell: test_cell_part0
import random
import numpy as np

# test 1
test_game1 = [[0,0,0] for elem in range(3)]
assert check_ttt(test_game1) == "No Result"

# test 2
test_game2 = [[1,1,1],[-1,-1,0],[0,0,0]]
assert check_ttt(test_game2) == "Circles (+1) Win"

# test 3
test_game3 = [[0,0,-1],[1,-1,1],[-1,1,0]]
assert check_ttt(test_game3) == "Crosses (-1) Win"

# test 4
test_game4 = [[0,0,-1],[1,-1,-1],[1,1,-1]]
assert check_ttt(test_game4) == "Crosses (-1) Win"

print("\n(Passed!)")


# In[16]:


# Test cell: test_cell_part1
import random
import numpy as np


def test_check_ttt():
    test_game_random = [[0,0,0] for elem in range(3)]
    boxes_filled = random.randint(0,8)
    num_circles = int(boxes_filled/2)

    circle_ind = random.sample(range(9),num_circles)
    cross_ind = random.sample([elem for elem in range(9) if elem not in circle_ind],(boxes_filled-num_circles))        

    for elem in circle_ind: test_game_random[int(elem/3)][elem%3] = 1
    for elem in cross_ind: test_game_random[int(elem/3)][elem%3] = -1
    print(np.array(test_game_random))
    print("\nYour Result: {}".format(check_ttt(test_game_random)))

    your_answer = check_ttt(test_game_random)
    if 3 in np.sum(test_game_random,axis=0) and -3 in np.sum(test_game_random,axis=0): pass
    elif 3 in np.sum(test_game_random,axis=1) and -3 in np.sum(test_game_random,axis=1): pass
    elif 3 in np.sum(test_game_random,axis=0) and -3 in np.sum(test_game_random,axis=1): pass
    elif 3 in np.sum(test_game_random,axis=1) and -3 in np.sum(test_game_random,axis=0): pass
    elif 3 in np.sum(test_game_random,axis=0): assert your_answer == "Circles (+1) Win"
    elif -3 in np.sum(test_game_random,axis=0): assert your_answer == "Crosses (-1) Win"
    elif 3 in np.sum(test_game_random,axis=1): assert your_answer == "Circles (+1) Win"
    elif -3 in np.sum(test_game_random,axis=1): assert your_answer == "Crosses (-1) Win"
    elif np.trace(test_game_random) == 3: assert your_answer == "Circles (+1) Win"
    elif np.trace(test_game_random) == -3: assert your_answer == "Crosses (-1) Win"
    elif np.flipud(test_game_random).trace() == 3: assert your_answer == "Circles (+1) Win"
    elif np.flipud(test_game_random).trace() == -3: assert your_answer == "Crosses (-1) Win"
    else: assert check_ttt(test_game_random) == "No Result"

print("testing function for random game states..")
for i in range(20):
    print("---------- Game State {} ----------".format(i))
    test_check_ttt()

print("\n(Passed!)")


# **Fin!** You've reached the end of this problem. Don't forget to restart the
# kernel and run the entire notebook from top-to-bottom to make sure you did
# everything correctly. If that is working, try submitting this problem. (Recall
# that you *must* submit and pass the autograder to get credit for your work!)
