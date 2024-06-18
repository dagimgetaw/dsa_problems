class Solution(object):
    def longestCommonPrefix(self, strs):

        shortest_string = min(strs, key=len)
        longest_common_prefix = ""

        for i, char in enumerate(shortest_string):
            for string in strs:
                if string[i] != char:
                    return(longest_common_prefix)
                    exit()
            longest_common_prefix += char
        return(shortest_string)
