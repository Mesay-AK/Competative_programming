class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counted=defaultdict(lambda:0)
        for i in nums:
            counted[i]+=1
            if counted[i]>len(nums)//2:
                return i