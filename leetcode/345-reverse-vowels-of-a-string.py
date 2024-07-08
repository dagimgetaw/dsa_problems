class Solution:
    def reverseVowels(self, s: str) -> str:
 
        vowel = []
        normal = []

        for char in s:
            if char in "aeiouAEIOU":
                vowel.append(char)
                normal.append("+")
            else:
                normal.append(char)

        vowel.reverse()

        index = 0
        for i in range(len(normal)):
            if normal[i] == "+":
                normal[i] = vowel[index]
                index += 1

        result = "".join(normal)

        return result
