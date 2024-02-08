class Solution(object):
    def subarraysDivByK(self, nums, k):
        subry = defaultdict(int)
        subry[0] = 1
        total = 0 
        result = 0
        for n in nums:
            total += n
            reminder = total%k
            result += subry[reminder]
            subry[reminder] +=1

        return result
        