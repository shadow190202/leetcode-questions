class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        water = 0
        for _ in range(len(height)):
            lower_side = min(height[i],height[j])
            water = max(water, lower_side*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water