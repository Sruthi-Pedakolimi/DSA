# LeetCode Problem 017: Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number
# Difficulty: Medium
# Solution:

class Solution(object):
    def getCombination(self, digits, letters_dict, combinations_list):
        if digits == "0" or digits == "":
            return combinations_list

        new_list = []
        print("Digits: ", digits)
        last_digit = int(digits) % 10
        digits = int(digits) // 10
        if last_digit != 1:
            alphabets = letters_dict.get(last_digit)
            for i in alphabets:
                if len(combinations_list) == 0:
                    new_list.append(i)
                else:
                    new_list.extend(list(map(lambda item: i + item, combinations_list)))

        return self.getCombination(str(digits), letters_dict, new_list)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        combinations_list = []
        return self.getCombination(digits, letters_dict, combinations_list)


