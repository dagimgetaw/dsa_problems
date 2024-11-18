from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        counter = Counter(stones)
        n = 0

        for char in jewels:
            n += counter[char]

        return n