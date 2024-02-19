class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        tovalid = 0
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)

            elif stack and stack[-1] == '(':
                stack.pop()
                
            else:
                tovalid += 1

        return tovalid + len(stack)


            