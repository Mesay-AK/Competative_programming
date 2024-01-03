class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        maxim=max(costs)
        
        arr=[0]*(maxim+1)
        total=0
        for i in range(len(costs)):
            arr[costs[i]]+=1
        
        
        for i in range(1,len(arr)):
            j=0
            while arr[i]>0 and j<arr[i] and coins-i>=0:
                coins-=i
                total+=1
                j+=1



        return total































         

