class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n=len(piles)
        piles.sort()
        i=n-2
        result=0
        for j in range(n/3):
            result+=piles[i]
            i-=2
        return result
        
