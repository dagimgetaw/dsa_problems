class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        index = []
        sorted_p = sorted(p)
        window = s[:k]


        if sorted(window) == sorted_p:
            index.append(0)

        for i in range(k, len(s)):
            window = window[1:] + s[i]

            if sorted(window) == sorted_p:
                index.append(i - k + 1)

        return index
