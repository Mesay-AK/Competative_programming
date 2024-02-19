class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        numbers = 0
        rabbits = Counter(answers)

        for i in rabbits:
            if i == 0:
                numbers += rabbits[i]
                continue

            elif rabbits[i] <= i + 1:
                numbers += i+ 1
            else:
                numbers += (ceil(rabbits[i]/(i+1)) * (i + 1))


        return numbers



