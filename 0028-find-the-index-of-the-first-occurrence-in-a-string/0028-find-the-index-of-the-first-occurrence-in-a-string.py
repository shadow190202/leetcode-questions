class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        result = 0
        if needle in haystack:
            result = haystack.find(needle)
        else:
            result = -1
        return result
