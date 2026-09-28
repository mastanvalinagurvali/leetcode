class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[-1]*n

        def robery(i):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            rob=nums[i]+robery(i+2)
            skip=robery(i+1)
            dp[i]=max(rob,skip)
            return dp[i]
        return robery(0)