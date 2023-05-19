"""
You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations.
"""
def minimizeArrayValue(self, nums: List[int]) -> int:
    """
    Time: No 
    Solve: Medium
    Difficulty: Medium(personally think is hard) 
    Comments: 
        I could tell it is a DP but the math behind it I will never able to see it. Is a pretty clean solution if you could think about the step
        of evening out all the value in the array. You need to round up, and seems like python2 has some problem with celiing function and truncation
        
    """
    res = total = nums[0]
    for i in range(1,len(nums)):
        total += nums[i]
        res = max(math.ceil(total/(i+1)),res)
    return res