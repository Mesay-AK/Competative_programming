class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        now= (num-3)/3
        res=[]
        if now.is_integer():
            now=int(now)
            res.append(now)
            res.append(now+1)
            res.append(now+2)
        return res