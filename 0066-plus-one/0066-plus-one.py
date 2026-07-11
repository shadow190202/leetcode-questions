class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = int(''.join(str(i) for i in digits)) + 1
        result = [int(i) for i in str(res)]
        return result
