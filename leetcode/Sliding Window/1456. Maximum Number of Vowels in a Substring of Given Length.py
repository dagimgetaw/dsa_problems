class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        s = list(s)
        window = s[:k]
        vowel = ['a','e','i','o','u']
        x, y = 0, 0

        for i in range(k):
            if s[i] in vowel:
                x += 1
        y = x

        for i in range(k, len(s)):
            if s[i - k] in vowel:
                x -= 1
            if s[i] in vowel:
                x += 1
            window.pop(0)
            window.append(s[i])
            y = max(x, y)

        return y   