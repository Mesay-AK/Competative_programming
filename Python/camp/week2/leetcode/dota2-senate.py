class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        D, R = deque(), deque()

        for i, vote in enumerate(senate):
            if vote == 'R':
                R.append(i)

            else:
                D.append(i)

        while R and D:
            pR = R.popleft()
            pD = D.popleft()

            if pR < pD:
                R.append(len(senate) + pD)
            else:
                D.append(len(senate) + pR)

        if R:
            return 'Radiant'

        else:
            return 'Dire'