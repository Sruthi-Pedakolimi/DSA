"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are
not equal to val

Change the array nums such that the first k elements of nums contain the elements which are not
equal to val. The remaining elements of nums are not important as well as the size of nums.
"""

class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        if val not in nums:
            return n

        count_val = nums.count(val)
        for i in range(count_val):
            nums.remove(val)
        return n - count_val