# LeetCode Problem 074: Search a 2D matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix
# Difficulty: Medium
# Solution:

class Solution(object):
    def binarySearch(self, arr, n, target):
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low = 0
        m = len(matrix)
        n = len(matrix[0])
        high = m-1
        while low <= high:
            mid = (low + high)//2
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][n-1] < target:
                low = mid + 1
            else:
                return self.binarySearch(matrix[mid], n, target)
        return False