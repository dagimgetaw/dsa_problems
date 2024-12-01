class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        if target == "z":
            return letters[0]

        letters.append(target)
        arr = list(set(letters))
        arr.sort()
        index = arr.index(target)

        if index + 1 == len(arr):
            return arr[0]
        else:
            return arr[index + 1]