class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = ['+', '-', '*', '/']
        s = []
        for i in tokens:
            if i not in a:
                s.append(int(i))
            else:
                d, h = s.pop(), s.pop()
                if i == '+':
                    s.append(h + d)
                elif i == '-':
                    s.append(h - d)
                elif i == '*':
                    s.append(h * d)
                else:
                    s.append(int(h / d))
        return s[0]