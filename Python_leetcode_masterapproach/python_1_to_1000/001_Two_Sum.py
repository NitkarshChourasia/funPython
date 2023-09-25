_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution.

# Maintain a mapping from each number to its index.
# Check if target - num has already been found.
# Time - O(n)
# Space - O(n) for the dictionary

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_to_index = {}           # key is number, value is index in nums
        print(num_to_index)

        for i, num in enumerate(nums):

            print(f"Target: {target}")
            print(f"Num: {num}, i: {i}")

            if target - num in num_to_index: # Because can't use the same element twice.
                return [num_to_index[target - num], i]
            print(f"1st Num to index: {num_to_index}")

            num_to_index[num] = i
            print(f"2nd Num to index: {num_to_index}")
        print(f"EOF: {num_to_index}")
        return []   # no sum


if __name__ == "__main__":
    # Test cases.
    # print(Solution().twoSum([2, 7, 11, 15], 9)) # [0, 1]
    # print(Solution().twoSum([3, 2, 4], 6)) # [1, 2]
    print(Solution().twoSum([6, 2, 4], 6)) # [1, 2]
    # print(Solution().twoSum([3, 3], 6)) # [0, 1]

    # # Additional test cases.
    # print(Solution().twoSum([0, 4, 3, 0], 0)) # [0, 3]
