class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        '''
        1 2 3 4
        0 1 2 3
        from  0 to 1  lets find the sum of all distance==10,
        find the distance fro 0 to 1==1 another round will be 10 - 1

        from 0 to 2 the distance will be 1 + 2 = 3 the counter clock wise distance will be 10 -3=7
        from 0 to 3 the distance will be 1 + 2 + 3 = 6 the counter clock wise distance will be 10 -4 =6 
        what if it starts from 3 to 4  the clock wise = 3 counter clock wise =10-3=7
        '''
        clock_wise=0
        total=sum(distance)
        
        for i in range(min(start,destination),max(start,destination)):
            clock_wise+=distance[i]
        minimum=min(clock_wise,total-clock_wise)
        
        return minimum