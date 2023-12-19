class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        union=set(fronts+backs)
        for f,b in zip(fronts, backs):
            if f == b:
                union.discard(f)
        return min(union,default=0)


        

