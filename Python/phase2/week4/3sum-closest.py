class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minim=float('inf')
        rslt=0
        nums.sort()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                summ=nums[i]+nums[j]+nums[k]
                if minim>abs(summ-target):
                    minim=abs(summ-target)
                    rslt=summ
                if summ-target>0:
                    k-=1
                elif summ-target<=0:
                    j+=1
        return rslt