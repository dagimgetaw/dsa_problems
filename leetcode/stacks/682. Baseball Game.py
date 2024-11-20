class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stk = []

        for i in operations:
            if i == "C":
                stk.pop()
            elif i == "D":
                stk.append(2 * stk[-1])
            elif i == "+":
                stk.append(stk[-1] + stk[-2])
            else:
                stk.append(int(i))

        return sum(stk)
