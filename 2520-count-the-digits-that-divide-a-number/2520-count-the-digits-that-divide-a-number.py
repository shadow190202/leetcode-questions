class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        st = str(num)
        count = 0
        for i in st:
            if num % int(i) == 0:
                count += 1
        return count