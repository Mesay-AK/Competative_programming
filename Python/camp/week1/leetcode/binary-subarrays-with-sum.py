class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        result, subrry, total = 0, defaultdict(int), 0
        subrry[0] = 1
        for n in nums:
            total += n
            result += subrry[total - goal]
            subrry[total] += 1 
    
        return result

