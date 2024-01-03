class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        mark={}
        for i in points:
            x, y = i[0]**2, i[1]**2
            d = (x+y)**0.5
            j=tuple(i)
            mark[j] = d
        
        def comparator(pts):
            i=tuple(pts)
            return mark[i]
        points.sort(key=comparator)

        return points[:k]
       

