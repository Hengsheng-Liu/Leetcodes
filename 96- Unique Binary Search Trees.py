def numTrees(n):
    """
    :type n: int
    :rtype: int

    Time: None
    Solve: No
    Difficulty: Medium  
    Comments: 
        If never study Catalan Numbers, I will never find the trend and the DP behind this question, I think this question is pure Math 
        and no coding involve. One thing I learn is that for i in range of () if is same number then the loop will not execute in which
        took me forever to debug. Pretty good DP question though. Tycially you could just cheap by applying using the Catalan formula 
    """
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1 
    for i in range(2,n+1):
        for j in range(1,i+1):
            dp[i] += dp[j-1]*dp[i-j]
    return dp[-1]
    """
    Comments: Oneliner
    def factorial(n):
        product = int(1) seems like python if you define as int it will fills in as a long type space(good to know)
        for i in range(1,n+1):
            product*=i
        return product
    def numTrees(self, n):
        :type n: int
        :rtype: int
        top = factorial(2*n)
        bottom = factorial(n+1)*factorial(n)
        ans = int(top/bottom)
        return ans 
    """
