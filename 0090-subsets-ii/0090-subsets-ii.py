class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        ds=[]
        nums.sort()
        def findsub(idx):
            ans.append(ds.copy())
            for i in range(idx,len(nums)):
                if i!=idx and nums[i]==nums[i-1]:
                    continue
                ds.append(nums[i])
                findsub(i+1)
                ds.pop()
        findsub(0)
        return ans