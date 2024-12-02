class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
            n = len(cost)
            prev1, prev2 = cost[1], cost[0]  
            
            for i in range(2, n):
                current = cost[i] + min(prev1, prev2)
                prev2, prev1 = prev1, current 

            return min(prev1, prev2)