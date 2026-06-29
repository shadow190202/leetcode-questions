class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {'(':')', '{':'}', '[':']'}
        for i in s:
            if i in dict:
                stack.append(i)
            elif stack and stack[-1] in dict and dict[stack[-1]] == i:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False