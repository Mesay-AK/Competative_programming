class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        for i in range(len(tickets)):
            if i == k:
                queue.append((tickets[i], True))
            else:
                queue.append((tickets[i], False))

        t = tickets[k]
        time = 0

        while t > 1:

            length = len(queue)
            
            for i in range(len(queue)):
                
                v, b = queue.popleft()
                if v > 1:
                    queue.append((v-1, b))
            
            time += length
            t-=1

        left = 0
        for i in range(len(queue)):
            if not queue[i][-1]:
                left += 1
            else:
                break 

        print(left)

        return time + left + 1

