# Problem Description: 
#   https://leetcode.com/problems/valid-parentheses/description
# Tags: #easy, #string, #stack 

class Solution:
    def isValid(self, input: str) -> bool:
        open_parentheses = ('(', '[', '{')
        end_parentheses = {')': '(', ']': '[', '}': '{'}
        stack: list[str] = []
        result = True
        
        # Edge case: if the input's length is not even
        if len(input) % 2 != 0:
            result = False
        else:
            for idx, char in enumerate(input):
                if char in open_parentheses:
                    stack.append(char)
                elif stack == [] or stack.pop() != end_parentheses[char]:
                    result = False
                    break
                continue
        if stack != []:
            result = False
        return result

        

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
#         output = s.isValid(input)
#         assert output == expected, f"input: {input}, output: {output}, expected: {expected}"