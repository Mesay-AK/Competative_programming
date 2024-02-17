class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        """
        Input: String of / and ...

        Output: string (simplified)

        """

        s=path.split('/')
        stack=[]
        for i in s:
            if i=='.'or i=='':
                pass
            elif i=='..':
                if stack: stack.pop()
            else:
                stack.append(i)
        return '/'+'/'.join(stack)



        