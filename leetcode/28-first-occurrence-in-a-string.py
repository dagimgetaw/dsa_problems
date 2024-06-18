class Solution(object):
    def strStr(self, haystack, needle):
        index = haystack.find(needle)
        if index >= 0:
            return(index)
        else:
            return(-1)
