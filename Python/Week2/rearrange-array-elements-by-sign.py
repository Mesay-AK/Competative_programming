class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        the_negatives=[]
        the_positives=[]
        result=[]
        for i in nums:
            if i<0:
                the_negatives.append(i)
            else:
                the_positives.append(i)
        for i in range(len(the_negatives)):
            result.append(the_positives[i])
            result.append(the_negatives[i])
        return result