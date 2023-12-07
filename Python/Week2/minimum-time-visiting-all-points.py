class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds=0
        for i in range(len(points)-1):
          x1,y1 = points[i]
          x2,y2 = points[i+1]
          distanceX= abs(x2-x1)
          distanceY= abs(y2-y1)
          seconds+=max(distanceX,distanceY)
        return seconds




        