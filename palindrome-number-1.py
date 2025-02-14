# Solution: without converting number into String

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge case:
        # - any negative number is not a Palindrome. Because when you reverse
        #   such number '-' comes to the end.
        # - Any number that ends with 0 is also never going to be Palindrome.
        #   Because, if you 10 has to be Palindrome then it needs to be written
        #   as 010, which is valid, but computer takes it as 10 and it also 10
        #   so... 

        if (x < 0) or (x != 0 and x % 10 == 0):
            return False
        
        half=0 # this will hold half of the input digits

        # The way we do it is: we don't need to reverse the complete number,
        # just the half of it is good enough. 
    
        # How do we reverse the number? we
        # use //(integer division) to get remaining digits(what's it called in
        # maths (quotient?)) and %(modulo) operator get last digit(reminder)

        # How do we know whether we've reversed exactly half the number?
        # When the original input == reversed number, then...
        while (x > half):
            half = (half * 10) + (x % 10)
            x = x // 10

        if x == half or half // 10 == x:
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
    (
        (0,),
        True,
    ),
    
]

if __name__ == "__main__":
    s = Solution()
    for input, expected in tests:
        out = s.isPalindrome(*input)
        assert out == expected, f"input: {input}, output: {out}, expected: \
                                {expected}"