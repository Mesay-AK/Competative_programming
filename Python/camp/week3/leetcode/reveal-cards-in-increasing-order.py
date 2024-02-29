class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort()
        q = deque(i for i in range(len(deck)))

        track = []
        print(q)

        while q:
            track.append(q.popleft())
            if q:
                q.append(q.popleft())

        result = [0] * len(deck)
        for i in range(len(deck)):
            result[track[i]] = deck[i]

        return result
























        # deck.sort()
        # indIn = deque(range(len(deck)))
        # indOut = []
        
        # while indIn:
        #     indOut.append(indIn.popleft())
        #     if indIn:
        #         indIn.append(indIn.popleft())
        # print(indIn)
        # result = [0]*len(deck)
        # for i, card in zip(indOut, deck):
        #     result[i] = card
        
        # return result



        