class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1=defaultdict(lambda:0)
        d2=defaultdict(lambda:0)
        for i in nums1:
            d1[i]+=1
        for i in nums2:
            d2[i]+=1
        result=[]
        for i in d1:
            minim=min(d1[i],d2[i])
            j=0
            while j<minim:
                result.append(i)
                j+=1
        return result
