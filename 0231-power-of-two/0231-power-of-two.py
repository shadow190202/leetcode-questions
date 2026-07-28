class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Best case
        return n > 0 and n & (n-1) == 0

        # Recursion

        # if n < 1:
        #     return False
        # elif n == 1:
        #     return True
        # elif n > 1 and  n%2 != 0:
        #     return False
        # return self.isPowerOfTwo(n//2)