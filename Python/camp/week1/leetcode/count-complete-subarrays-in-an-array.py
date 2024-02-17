class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        complete = 0
        n = len(nums)
        k = len(set(nums))
        
        for i in range(n):
            subarrSet = set()

            for j in range(i, n):
                subarrSet.add(nums[j])

                if len(subarrSet) == k:
                    complete += 1
        
        return complete













        # res=0
        # for i in nums:
        #     d[i]+=1
        # for i in range(len(nums)):
        #     r=len(nums)-1
        #     dup=copy.deepcopy(d)
        #     while True and i<=r:
        #         dup[nums[r]]-=1
        #         res+=1
        #         if dup[nums[r]]==0:
        #             break
        #         r-=1
        #     d[nums[i]]-=1
        #     if d[nums[i]]==0:
        #         return res
        # return res