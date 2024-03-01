class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        nums = {'2':'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        N = len(digits)

        combined = []
        def combine(i):

            if i >= N:
    
                result.append(''.join(combined))
                return

            n = digits[i]
            stg_ = nums[n]
            
            for j in range(len(stg_)):
                
                combined.append(stg_[j])
            
                combine(i+1)

                combined.pop()
            
        combine(0)

        return result

            
















































        result = []

        # assign = {
        #     "2": ['a','b','c'],
        #     "3": ['d','e','f'],
        #     "4": ['g','h','i'],
        #     "5": ['j','k','l'],
        #     "6": ['m','n','o'],
        #     "7": ['p','q','r','s'],
        #     "8": ['t','u','v'],
        #     "9": ['w', 'x', 'y','z']
        # }

        # def backtrack(i,stg):
        #     if i >= len(digits):
        #         if(stg):
        #             result.append(stg)
        #         return
        #     for j in assign[digits[i]]:
        #         backtrack(i+1,stg+j)
            
        # backtrack(0,"")
        
        # return result