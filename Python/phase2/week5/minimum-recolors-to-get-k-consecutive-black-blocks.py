class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites=0
        minim=len(blocks)
        for b in range(k):
            if blocks[b] == 'W':
                whites += 1
        
        left=0
        for b in range(k,len(blocks)):
            minim = min(minim, whites)
            if blocks[left] == 'W':
                whites -= 1
            if blocks[b] == 'W':
                whites += 1
            left+=1
        minim = min (minim, whites)

        return minim