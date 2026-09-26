class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans=[]
        ds=[]
        def findcombination(idx,target):
            if target==0:
                ans.append(ds.copy())
                return
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                ds.append(candidates[i])
                findcombination(i+1,target-candidates[i])
                ds.pop()
        findcombination(0,target)
        return ans
