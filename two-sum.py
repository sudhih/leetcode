# Problem Description: https://leetcode.com/problems/two-sum/description/
# Tags: #easy, #array, #hash-table

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = None
        for i in range(len(nums)):
            lhs = nums[i]
            for index, num in enumerate(nums):
                if i == index:
                    continue
                if lhs + num == target:
                    result = [i, index] 
                    break
            if result:
                break

        return result
                

tests = [
    (
        ([2,7,11,15], 9),
        [0, 1],
    ),
    (
        ([3, 2, 4], 6),
        [1, 2],
    ),
    (
        ([3, 3], 6),
        [0, 1],
    ),
    (
        ([2, 7, 11, 15], 13),
        [0, 2],
    ),
]

if __name__ == "__main__":
    s = Solution()
    for input, expected in tests:
        output = s.twoSum(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"