class Solution:
    def twoSum(self, nums, target):
        hashtable = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hashtable:
                return [hashtable[x], i]
            hashtable[nums[i]] = i

tests = [
    (
        ([2, 7, 11, 15], 9),
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
