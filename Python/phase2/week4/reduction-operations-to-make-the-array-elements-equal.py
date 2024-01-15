class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        count=0
        track=defaultdict(int)

        for i in range(1,len(nums)):
            if nums[i]!=nums[0]:
                track[nums[i]] += 1

        tracksorted=[i for i in track] 
        tracksorted.sort()

        for i in range(len(tracksorted)):
            count += (i+1)*track[tracksorted[i]]
        
        return count