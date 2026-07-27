class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = n
        prd, sum_n = 1,0

        while temp > 0:
            digit = temp % 10
            prd *= digit
            sum_n += digit
            temp//=10
        return prd - sum_n