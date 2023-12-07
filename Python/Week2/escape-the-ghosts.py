class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
      distance=abs(target[0])+abs(target[1])
      for i in range(len(ghosts)):
        ghosts_distance=abs(ghosts[i][0]-target[0])+abs(ghosts[i][1]-target[1])
        if distance>=ghosts_distance:
          return False
        
      return True
