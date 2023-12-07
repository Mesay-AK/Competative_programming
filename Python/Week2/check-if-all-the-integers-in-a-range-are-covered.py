class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        the_set=set()
        for i in ranges:
            start,end=i[0],i[1]
            for j in range(start,end+1):
                the_set.add(j)
        for i in range(left,right+1):
            if i  not in the_set:
                return False
        return True