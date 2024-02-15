class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        fives, tens, = 0, 0 
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                fives -=1
                tens += 1
                if fives < 0:
                    return False
            elif bill == 20:
                fives -= 1
                tens -= 1
                if tens < 0:
                    tens +=1
                    fives -= 2
                if fives < 0:
                    return False
                
        return True
        