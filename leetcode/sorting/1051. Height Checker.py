class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        expected = []

        for i in heights:
            expected.append(i)

        expected.sort()
        not_match = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                not_match += 1

        return not_match