class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        the_list=[]
        i,j=0,0
        while i<len(s):
            if j<len(spaces) and i==spaces[j] :
                the_list.append(' ')
                the_list.append(s[i])
                j+=1
            else:
                the_list.append(s[i])
            i+=1
        return ''.join(the_list)
