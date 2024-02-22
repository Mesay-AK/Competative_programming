class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        def compare(arr):
                
            return arr[0] - arr[1]


        costs.sort(key = compare)
        minim =0

        for c in range(len(costs)//2):
            minim += costs[c][0]

        for c in range(len(costs)//2, len(costs)):
            minim += costs[c][1]

        return minim