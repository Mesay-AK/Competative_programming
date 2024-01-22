class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dicts = {}
        minim = float('inf')

        for i in range(len(cards)):
            if cards[i] in dicts:
                minim = min(minim, i - dicts[cards[i]] + 1)
            dicts[cards[i]] = i
        
        return minim if minim != float('inf') else -1





    
