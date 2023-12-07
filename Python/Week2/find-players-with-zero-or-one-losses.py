class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        winner = defaultdict(lambda:0)
        loser = defaultdict(lambda:0)

        for i in range(len(matches)):
            winner[matches[i][0]]+=1
            loser[matches[i][1]]+=1

        result=[[],[]]
        for j in winner:
          if j not in loser:
            result[0].append(j)

        for j in loser:
          if loser[j]==1:
            result[1].append(j)
            
        result[0].sort()
        result[1].sort()
        return result
