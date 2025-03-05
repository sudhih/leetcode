# Problem Description: 
#   https://leetcode.com/problems/valid-parentheses/description
# Tags: #easy, #string, #stack

class Solution:
    def isValid(self, input):
        stack = []
        close_to_open = { ']':'[', ')':'(', '}':'{'}
        for c in input:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

# `pyleet` tests here
tests = [
    (
        ("()",),
        True,
    ),
    (
        ("()[]{}",),
        True,
    ),
    (
        ("(]",),
        False,
    ),
    (
        ("([])",),
        True,
    ),
    (
        ("]",),
        False,
    ),
    
]



# Want to debug? uncomment the below
# if __name__ == '__main__':
#     s = Solution()
#     for input, expected in tests:
#         output = s.<methodName>(*input)
#         assert output == expected, f"input: {input}, output: {output}, expected: {expected}"