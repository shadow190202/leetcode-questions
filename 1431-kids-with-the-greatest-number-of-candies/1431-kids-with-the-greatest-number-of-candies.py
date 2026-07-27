class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        req = []
        for i in candies:
            req.append(i + extraCandies >= max(candies))
        return req
