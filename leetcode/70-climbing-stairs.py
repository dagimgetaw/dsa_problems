class Solution(object):
    def climbStairs(self, n):

        if n == 1:
            return 1
        if n == 2:
            return 2

        t = 1
        o = 2

        for i in range(2, n):
            s = t + o
            t = o
            o = s
        return s

        