class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        prefix = [0] * 1001

        for passengers, _from, _to in trips:
            prefix[_from] += passengers
            prefix[_to] -= passengers

      
        for px in range(1,1001):
            prefix[px] = prefix[px-1] + prefix[px]


        for i in range(1001):
            if prefix[i] >capacity:
                return False
        return True