class Solution:
    def printVertically(self, s: str) -> List[str]:
            my_list=s.split(' ')
            maximum=0
            for i in my_list:
                maximum=max(maximum,len(i))
            i=0
            result=[]
            while i<maximum:
                stg=''
                for j in my_list:
                    if len(j)<=i:
                        stg+=' '
                    else:
                        stg+=j[i]
                to_append=stg.rstrip()
                result.append(to_append)
                i+=1
            
            return result