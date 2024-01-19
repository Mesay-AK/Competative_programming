class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        l, total = 0, sum(cardPoints[len(cardPoints)-k:])
        maxim = 0

        for r in range(len(cardPoints)-k,len(cardPoints)):
            maxim = max(total, maxim)
            total -= cardPoints[r]
            total += cardPoints[l]
            l+=1

        maxim = max(total, maxim)
        return maxim





        