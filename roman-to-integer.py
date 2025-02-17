# Problem Description: 
#   https://leetcode.com/problems/roman-to-integer/description
# Tags: #easy, #hashtable, #math, #string
from types import SimpleNamespace
symbols = SimpleNamespace(
    I=1, V=5, X=10, L=50, C=100, D=500, M=1000
)

class Solution:
    def romanToInt(self, input):
        i, sum, size = 0, 0, len(input)
        while(i<size):
            current = symbols.__getattribute__(input[i])
            try:
                after = symbols.__getattribute__(input[i+1])
            except IndexError:
                after = current
            if current < after:
                sum += after - current
                i += 2
            else:
                sum += current
                i +=1
        return sum


# `pyleet` tests here
tests = [
    (
        ("III",),
        3,
    ),
    (
        ("LVIII",),
        58,
    ),
    (
        ("MCMXCIV",),
        1994,
    ),
    
]



# Want to debug? uncomment the below
if __name__ == '__main__':
    s = Solution()
    for input, expected in tests:
        output = s.romanToInt(*input)
        assert output == expected, f"input: {input}, output: {output}, expected: {expected}"