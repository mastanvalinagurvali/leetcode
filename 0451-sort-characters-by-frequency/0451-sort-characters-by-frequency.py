class Solution:
    def frequencySort(self, s: str) -> str:
        hm={}
        for i in range(len(s)):
            if s[i] in hm:
                hm[s[i]]+=1
            else:
                hm[s[i]]=1
        arr=sorted(hm,key=hm.get,reverse=True)
        ans=""
        for ch in arr:
            ans+=ch*hm[ch]
        return ans
