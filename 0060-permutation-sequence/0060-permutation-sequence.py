class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact=1
        number=[]
        for i in range(1,n+1):
            fact=fact*i
            number.append(i)
        fact=fact//n
        ans=""
        k=k-1
        while True:
            ans=ans+str(number[k//fact])
            number.pop(k//fact)
            if len(number)==0:
                break
            k=k%fact
            fact=fact//len(number)
        return ans