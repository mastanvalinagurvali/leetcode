class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        def findcombinations(ind,target,ds):
            if ind==len(candidates):
                if target==0:
                    ans.append(ds.copy())
                return
            if candidates[ind]<=target:
                ds.append(candidates[ind])
                findcombinations(ind,target-candidates[ind],ds)
                ds.pop()
            findcombinations(ind+1,target,ds)
        findcombinations(0,target,[])
        return ans