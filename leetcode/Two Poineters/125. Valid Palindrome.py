class Solution:
    def isPalindrome(self, s: str) -> bool:

        text = []
        symbol = "!@#$%^&*()}{[].\" /;,|`'<>?:_-=+\\"

        for char in s:
            if char in symbol:
                pass
            else:
                text.append(char.lower())

        text = "".join(text)
        left = 0
        right = len(text) - 1

        while left < right:
            if text[left] == text[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

        # reverse = text[::-1]
        # if text == reverse:
        #     return True
        # else:
        #     return False

