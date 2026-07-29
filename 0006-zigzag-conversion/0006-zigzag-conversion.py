class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
            
        row = [""] * numRows
        curr = 0
        going = False
        for ch in s:
            row[curr] += ch
    
            if curr == 0 or curr == numRows -1:
                going = not going
        
            if going:
                curr += 1
            else:
                curr -= 1
        return "".join(row)