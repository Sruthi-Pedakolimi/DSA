# LeetCode Problem 151: Reverse Words in a String
# Link: https://leetcode.com/problems/reverse-words-in-a-string
# Difficulty: Medium
# Solution:

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse_str = ""
        words = s.split()
        for word in words:
            if word != " ":
                reverse_str = word + " " + reverse_str

        return reverse_str.strip()
