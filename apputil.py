# Exercise 1 

import numpy as np

def ways(n):
    '''
    Given an amount n (in cents), return the number of ways
    to make change using only pennies (1¢) and nickels (5¢).
    '''
    
    count = 0
    
    # Number of nickels can range from 0 up to n//5
    for nickels in range(n // 5 + 1):
        # Remaining amount will be made with pennies
        pennies = n - (nickels * 5)
        if pennies >= 0:
            count += 1
    
    return count

# Exercise 2

import numpy as np

# Part 1: Student with the lowest score
def lowest_score(names, scores):
    '''
    Return the name of the student with the lowest test score.
    Works for both Python lists and NumPy arrays.
    '''
    names = np.array(names)
    scores = np.array(scores)
    
    index = np.argmin(scores)
    return names[index]

# Part 2: Names sorted in descending order of scores
def sort_names(names, scores):
    '''
    Return names sorted in descending order of scores.
    Works for both Python lists and NumPy arrays.
    '''
    names = np.array(names)
    scores = np.array(scores)
    
    sorted_indices = np.argsort(scores)[::-1]  # descending order
    return list(names[sorted_indices])