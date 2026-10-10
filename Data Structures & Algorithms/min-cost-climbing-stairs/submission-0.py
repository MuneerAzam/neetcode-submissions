class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 
        l=len(cost)
        dp=[0]*(l+2)
        dp[0],dp[1]=cost[0],cost[1]        
        for i in range(2,l):
            dp[i]=min(cost[i]+dp[i-1],cost[i]+dp[i-2])
        dp[l]=min(dp[l-1],dp[l-2])
        return dp[l]