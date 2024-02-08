class Solution(object):
    def subarraySum(self, nums, k):

        result = 0
        total = 0
        subrry = {0:1} 
        for n in nums:
            total += n
            if total - k in subrry:
                result += subrry[total - k]
            if total not in subrry:
                subrry[total] = 1
            else:
                subrry[total] += 1 
    
        return result










    












