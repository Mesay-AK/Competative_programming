class Solution:
    def interpret(self, command: str) -> str:
        '''using a stack to append each element and check it 
        '''
        stg=''
        for i,j in enumerate(command):
            if j=='G':
                stg+='G'
            elif j=='(':
                continue
            elif j==')' and command[i-1]=='(':
                stg+='o'
            elif j==')' and command[i-1]=='l':
                stg+='al'
        return stg

