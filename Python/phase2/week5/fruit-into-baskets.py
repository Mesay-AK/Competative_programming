class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dicts = defaultdict(int)

        l, r, total, maxim= 0, 0, 0, 0
        while r < len(fruits):
            dicts[fruits[r]] += 1
            total += 1

            while len(dicts)>2:
                dicts[fruits[l]] -= 1
                total -= 1
                if dicts[fruits[l]] == 0:
                    del(dicts[fruits[l]])
                l += 1

            maxim = max(maxim, total)
            
            r +=1

        return maxim
