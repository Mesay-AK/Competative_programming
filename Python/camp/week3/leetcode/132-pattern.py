class Solution(object):
    def find132pattern(self, nums):

        stack = []

        minim = float('inf')

        for i in nums:
             
            while stack and i>= stack[-1][0]:
                stack.pop()
            
            if stack and i > stack[-1][1]:
                return True

            stack.append([i, minim])
            minim = min(minim, i)

        return False

                 

            

        


        







