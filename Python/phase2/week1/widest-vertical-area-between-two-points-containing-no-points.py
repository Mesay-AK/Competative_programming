class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        maxim=0
        for i in range(1,len(points)):
            width=points[i][0]-points[i-1][0]
            maxim=max(maxim,width)
        return maxim
        