"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

def uniqueOccurrences(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    Time:Too quick 
    Solve: yes
    Difficulty: Easy 
    Comments: 
        Pretty easy question using dict to store all the appearance and then use set to check whether there is repetition or not. 
    """
    my_dict = {}
    my_set = set()
    for x in arr:
        my_dict[x] = my_dict.setdefault(x, 0) + 1
    for key in my_dict:
        if my_dict[key] in my_set:
            return False 
        else:
            my_set.add(my_dict[key])
    return True 