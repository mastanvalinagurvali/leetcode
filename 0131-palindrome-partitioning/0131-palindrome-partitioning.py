class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def part(idx,s,res,path):
            if idx==len(s):
                res.append(path[:])
                return
            for i in range(idx,len(s)):
                if palindrome(s,idx,i):
                    path.append(s[idx:i+1])
                    part(i+1,s,res,path)
                    path.pop()
        def palindrome(s,st,end):
            while st<=end:
                if s[st]!=s[end]:
                    return False
                st+=1
                end-=1
            return True
        res=[]
        path=[]
        part(0,s,res,path)
        return res