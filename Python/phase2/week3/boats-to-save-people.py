class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        j=0
        
        for i in range(len(people)-1,-1,-1):
            
            if j<=i and people[j]+people[i]<=limit:
                boats+=1
                i-=1
                j+=1
            elif j<=i:
                
                boats+=1
                i-=1
        return boats
