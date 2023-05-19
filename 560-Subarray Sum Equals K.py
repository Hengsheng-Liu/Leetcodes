"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    Time: None
    Solve: No
    Difficulty: Medium 
    Comments: 
    Pretty cool solution, something I realized in this question is that, the prefix sum hashmap stores all the sub-arry if you do it simultaneously.
    the dictonary all the combinations of value before this index. if you aim for some value, is like a undo method. like How many way 
    I could undo to get the value that I want. 
    """
    prefix = {}
    sum = 0
    count = 0
    for num in nums:
        sum+=num 
        need = sum - k # The sum is the prefix sum; k is the goal; This line is telling what value I need to undo to get k
        if need in prefix: # The HashMap already store how many sub-arry that has this value so we could undo it. 
            count += need 
        prefix[num] = prefix.setdefault(num, 0) + 1
    return count 
    