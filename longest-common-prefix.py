# Problem Description: 
#   https://leetcode.com/problems/longest-common-prefix/description
# Tags: #easy, #string, #trie

class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_str, length, index = "", -1, -1
        for idx, istr in enumerate(strs):
            if idx == 0:
                shortest_str, length, index = istr, len(istr), idx
                continue
            if len(istr) < length:
                shortest_str, length, index = istr, len(istr), idx

        lcp = ""
        for i, c in enumerate(shortest_str):
            for input in strs:
                if input[i] != c:
                    return lcp
            lcp += c
        return lcp



# `pyleet` tests here
tests = [
    (
        (["flower", "flight", "flow"],),
        "fl",
    ),
    (
        (["dog", "racecar", "car"],),
        "",
    ),
    (
        (['a'],),
        "a",
    ),
    (
        (['cir', 'car'],),
        "c",
    ),
    (
        (["reflower","flow","flight"],),
        ""
    ),
    (
        (["aa","ab"],),
        "a"
    ),
    (
        ([""],),
        "",
    ),
    (
        (["ab", "a"],),
        "a",
    ),
    
    
    
]


# Want to debug? uncomment the below
# if __name__ == '__main__':
#     s = Solution()
#     for input, expected in tests:
#         output = s.longestCommonPrefix(*input)
#         assert output == expected, f"input: {input}, output: {output}, expected: {expected}"