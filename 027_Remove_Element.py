# LeetCode Problem 027: Remove Element
# Link: https://leetcode.com/problems/remove-element
# Difficulty: Easy
# Solution:

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