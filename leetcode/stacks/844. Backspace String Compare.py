class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stk1 = []
        stk2 = []

        for i in s:
            if i == "#":
                if len(stk1) == 0:
                    pass
                else:
                    stk1.pop()
            else:
                stk1.append(i)

        for i in t:
            if i == "#":
                if len(stk2) == 0:
                    pass
                else:
                    stk2.pop()
            else:
                stk2.append(i)


        return stk1 == stk2