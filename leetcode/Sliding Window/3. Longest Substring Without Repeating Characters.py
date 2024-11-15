class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        if len(s) == 0:
            return 0
        arr = s[0]
        arr = list(arr)
        result = 1

        for i in range(1, len(s)):
            y = s[i]
            if y not in arr:
                arr.append(y)
                result = max(result, len(arr))
            else:
                r = arr.index(y)
                arr = arr[r+1:]
                arr.append(y)
                result = max(result, len(arr))

        return result