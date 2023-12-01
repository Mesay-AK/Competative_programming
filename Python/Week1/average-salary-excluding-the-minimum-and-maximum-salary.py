class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total=0
        length=len(salary)
        for i in salary[1:length-1]:
            total+=i
        return total/(length-2)
        
