class Solution:
    def scoreOfString(self, s: str) -> int:

        total = 0
        asci = []

        for i in range(len(s)):
            value = ord(s[i])
            asci.append(value)

        n = 0

        while n != len(asci) - 1:
            total += abs(asci[n] - asci[n + 1])
            n += 1
        return total