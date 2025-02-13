# LeetCode Problem 347: Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements
# Difficulty: Medium
# Solution:
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency_list = []
        counter = Counter(nums)
        sorted_counter = counter.most_common()
        for i in range(k):
            frequency_list.append(sorted_counter[i][0])
        return frequency_list


