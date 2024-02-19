class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key = lambda x: (x[0], x[1]) )
        start = points[0][0]
        end_ = points[0][1]
        arrow = 1

        for bln in range(1,len(points)):
            if points[bln][0] <= end_:
                end_= min(points[bln][1], end_)
            else:
                start = points[bln][0]
                end_ = points[bln][1]
                arrow += 1

        return arrow


