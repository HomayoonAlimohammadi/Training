from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = sorted(nums1+nums2)
        if len(final) % 2 == 0:
            return (final[len(final)//2-1]+final[len(final)//2])/2
        return float(final[len(final)//2])
