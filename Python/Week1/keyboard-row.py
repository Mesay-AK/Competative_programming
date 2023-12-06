class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        '''
        create a dictionary whose key is a number and it's value is a string of letters in it's row. check the row of the first letter in each word and check the rest of the string if all are in the same row...
        '''
        rows={1:"qwertyuiop",2:"asdfghjkl",3:"zxcvbnm"}
        the_same=[]

        for word in words:
            
           
            if word.lower()[0] in rows[1]:
                
                
                for letter in word[1:]:
                    
                    if letter.lower() not in rows[1]:
                        break
                else:
                    the_same.append(word)
                    
            elif word.lower()[0] in rows[2]:
                
                for letter in word[1:]:
                    
                    if letter.lower() not in rows[2]:
                        break
                else:
                    the_same.append(word)
            else:
                
                for letter in word[1:]:
                   
                    if letter.lower() not in rows[3]:
                        break
                else:
                    the_same.append(word)
            
                
        return the_same



































        # for i in range(len(words)):
        #     if words[i][0] in rows[1]:
        #         j=1
        #         while j<len(words[i]):
        #             if words[i][j] not in rows[1]:
        #                 break
        #             j+=1
        #         else:
        #             the_same.append(words[i])
                  
        #     elif words[i][0] in rows[2]:
        #         j=1
        #         while j<len(words[i]):
        #             if words[i][j] not in rows[2]:
        #                 break
        #             j+=1
        #         else:
        #             the_same.append(words[i])
        #     else:
        #         j=1
        #         while j<len(words[i]):
        #             if words[i][j] not in rows[3]:
        #                 break
        #         else:
        #             the_same.append(words[i])
        
        # return the_same

