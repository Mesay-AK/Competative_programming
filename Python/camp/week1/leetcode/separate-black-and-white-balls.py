class Solution:
    def minimumSteps(self, s: str) -> int:
        
        separate = list(s)
        result = 0
        r, l = len(s) - 1, 0
        while l<r:
            if separate[l] == '1' and separate[r] == '0':
                result += (r-l)
                separate[l], separate[r] = separate[r], separate[l] 
                r -= 1
            elif separate[l] == '0':
                l += 1
            else:
                r -= 1

        return result
            
            

