class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        '''
        the steps taken, the returning=index+1 ...
        subtruct from capacity at every step
        check if the capacity is greater or equal to 0
        if so, take the step and increment 1
        else increment the step by (index+1)
        '''
        steps=1
        amount=capacity

        for i in range(len(plants)-1):
            amount=amount-plants[i]
            if amount-plants[i+1]>=0:
                steps+=1
            else:
                steps+=(i+1)
                steps+=(i+2)
                amount=capacity     
        return steps
        