# LeetCode Problem 035: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position
# Difficulty: Easy
# Solution:

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        insertion_index = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= target:
                high = mid - 1
                insertion_index = mid
            else:
                low = mid + 1
        return insertion_index
