class Solution:
    def isHappy(self, n: int) -> bool:
        while n>9:
            sn=str(n)
            DictS={}
            n=0
            for i in range(len(sn)):
                DictS[i]=int(sn[i])
                n=n+(DictS[i])**2
        if n==1 or n==7:
            return True
        elif (n>1 and n<=9 ) or n==0:
            return False