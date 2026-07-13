class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        fib = []
        for i in range(n+1):
            fib.append(a)
            a, b = b, a + b
        return fib[n] + fib[n-1]


        