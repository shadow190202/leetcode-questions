class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Best Approach
        a,b,c = 0,1,1
        for _ in range(n):
            a,b,c = b,c,a+b+c
        return a

        #  Recursion
        # if n < 2:
        #     return n
        # elif n == 2:
        #     return 1
        # return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
