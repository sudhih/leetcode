# Problem Descrption:
# https://leetcode.com/problems/palindrome-number/description/
# Tags: #easy, #math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # converting number to string to enable reversing of the number
        if x < 0:
            return False

        y = str(x)
        y = int(y[::-1])
        if x == y:
            return True
        else:
            return False


tests = [
    (
        (121,),
        True,
    ),
    (
        (10,),
        False,
    ),
    (
        (-121,),
        False,
    ),
]