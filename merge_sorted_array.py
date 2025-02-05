"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        new_arr = []
        while i <= m - 1 and j <= n - 1:
            if nums1[i] < nums2[j]:
                new_arr.append(nums1[i])
                i = i + 1
            else:
                new_arr.append(nums2[j])
                j = j + 1

        if j <= n - 1:
            new_arr.extend(nums2[j:])

        if i <= m - 1:
            new_arr.extend(nums1[i:m])

        for k in range(m + n):
            nums1[k] = new_arr[k]