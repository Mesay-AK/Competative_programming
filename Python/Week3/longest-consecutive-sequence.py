class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        to_sort=set(nums)
        longest=0
        for i in nums:
            if (i-1) not in to_sort:
                count=0
                while (i+count) in to_sort:
                    count+=1
                longest=max(count,longest)
        return longest
