class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        to_str = str(x)
        if to_str[0] == "-":
            reversed_str = to_str[0] + to_str[:0:-1]
        else:
            reversed_str = to_str[::-1]
        reversed_int = int(reversed_str)
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        return reversed_int