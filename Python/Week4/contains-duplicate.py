class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=defaultdict(lambda:0)
        for num in nums:
            if num in d:
                return True
            d[num]+=1
        return False