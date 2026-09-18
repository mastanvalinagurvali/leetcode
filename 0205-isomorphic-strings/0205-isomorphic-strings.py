class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm={}
        hm2={}
        for i in range(len(s)):
            if s[i] in hm:
                if hm[s[i]]!=t[i]:
                    return False
            else:
                hm[s[i]]=t[i]
            if t[i] in hm2:
                if hm2[t[i]]!=s[i]:
                    return False
            else:
                hm2[t[i]]=s[i]
        return True