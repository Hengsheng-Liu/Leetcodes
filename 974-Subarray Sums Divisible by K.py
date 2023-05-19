"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.

"""

def subarraysDivByK(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    Time:No
    Solve: Medium
    Difficulty: Medium(personally think is hard) 
    Comments: 
        I will cry if this question is in my interview, like this is not a CS problem, more like mathematical thinking. I come with O(N^2)
        and the run time just kaboom. N square is easy to come up and O(N) solution just bring this queston to another level and LC expect a
        O(N) solution. 
    """
    """My solution
    subarrays = []
    n = len(nums)
    count = 0 
    for i in range(n):
        subarray = []
        list_sum = 0 
        for j in range(i, n):
            list_sum+=nums[j]
            if list_sum % k == 0:
                count+=1 
            subarray.append(nums[j])
            #subarrays.append(subarray[:])  # Make a copy of the subarray
    #print(subarrays)
    return count
    """
    """
    Comments: offical solution feels like a Bull shit math question. is like a DP question 
    """
    n = len(nums)
    count = 0
    prefix = 0
    remainder = [0]*k
    remainder[0] = 1
    for num in nums:
        # If they have same remainder that mean in the subarray 
        #prefix[current num] = C*k + remainder
        # if the remainder show up again that mean C is bigger than previous C thus there the
        # is a value that makes the subarry divisible by k 
        prefix = (prefix + num % k + k) % k
        count += remainder[prefix]
        remainder[prefix]+=1; 
    return count 