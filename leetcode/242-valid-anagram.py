class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        word1 = sorted(s.lower())
        word2 = sorted(t.lower())

        if word1 == word2:
            return True
        else:
            return False