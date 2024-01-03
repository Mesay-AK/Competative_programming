class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:


        maxim=0

        costs.sort()

        for i in range(len(costs)):
            if coins-costs[i]>=0:
                maxim+=1
                coins-=costs[i]
            else:
                break
        return maxim































         

