class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        result=[]
        frequency=defaultdict(lambda:0)
        for number in nums:
            frequency[number]+=1
        for number in frequency:
            if frequency[number]>len(nums)/3:
                result.append(number)
        return result
