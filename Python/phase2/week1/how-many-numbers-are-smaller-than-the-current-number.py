class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[]
        for i in range(n):
            c=0
            for j in range(n):
                if i!=j and nums[j]<nums[i]:
                    c+=1
            a.append(c)
        return a