class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
        ans=[]
        for i in range(len(s)):
            row=startPos[0]
            col=startPos[1]
            count=0
            for j in range(i,len(s)):
                if s[j]=='R':
                    col+=1
                elif s[j]=='L':
                    col-=1
                elif s[j]=='D':
                    row+=1
                elif s[j]=='U':
                    row-=1
                if row<0 or row>=n or col<0 or col>=n:
                    break
                count+=1
            ans.append(count)
        return ans