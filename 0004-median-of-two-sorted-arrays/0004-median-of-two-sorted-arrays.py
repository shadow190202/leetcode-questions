class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3 = sorted(nums1+nums2)
        mid = len(num3)//2
        if len(num3) % 2 == 0:
            req = float(num3[mid] + num3[mid - 1])/2
            return req
        else:
            return num3[mid]