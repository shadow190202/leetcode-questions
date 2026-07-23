class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        arr = []
        lower_side = 0
        for _ in range(len(height)):
            lower_side = min(height[i],height[j])
            area = lower_side*(j-i)
            if height[i] < height[j]:
                i += 1
                arr.append(area)
            else:
                j -= 1
                arr.append(area)
        return max(arr)