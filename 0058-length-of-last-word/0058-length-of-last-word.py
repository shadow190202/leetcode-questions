class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        req = s.strip().split(" ")
        return len(req[-1])
            
            