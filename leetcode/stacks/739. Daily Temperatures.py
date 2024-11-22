class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       
        stk = [0] * len(temperatures)  
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                stk[prev_index] = i - prev_index
            stack.append(i) 


        return stk
