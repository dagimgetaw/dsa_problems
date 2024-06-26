class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return(False)
        rev = 0
        num = x
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        return(rev == num)
        
