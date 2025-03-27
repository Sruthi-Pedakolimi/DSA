# LeetCode Problem 153: Find Minimum in Rotated Sorted Array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
# Difficulty: Medium
# Solution:

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        min_element = float('inf')
        while (low <= high):
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                if nums[low] < min_element:
                    min_element = nums[low]
                low = mid + 1
            elif nums[mid] <= nums[high]:
                if nums[mid] < min_element:
                    min_element = nums[mid]
                high = mid - 1
        return min_element
