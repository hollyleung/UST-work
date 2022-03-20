from typing import List

class Solution:
    def minPower(self,  cost: List[int]) -> int:
        cost.append(0)                 
        
        for i in range(2,len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
    
        return cost[-1]

with open('q5.txt') as f:
    lines = list(map(int, f.read().splitlines()))    
    
p = Solution()
p.minPower(lines)

