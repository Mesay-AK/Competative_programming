class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')': '(', '}':'{', ']':'['}
        for i in s:
            if i not in check:
                stack.append(i)
            else:
                if not stack or stack[-1] != check[i]:
                    return False
                else:
                    stack.pop()

        return stack == []

