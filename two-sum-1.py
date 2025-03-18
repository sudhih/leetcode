class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, lhs in enumerate(nums):
            for j in range(i+1, len(nums)):
                rhs = nums[j]
                if lhs + rhs == target:
                    return [i, j]
                
                

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
        assert output == expected, f"input: {input}, output: {output}, expected: {expected}" 