class Solution:
    def freqAlphabets(self, s: str) -> str:

        stg=''
        i=0
        while i<len(s):
            if (i+2)<len(s) and s[i+2]=='#':
                now = s[i:i+2]
                stg+=chr(96+int(now))
                i+=3
            else:
                stg+=chr(96+int(s[i]))
                i+=1
        return stg















      
                
                
