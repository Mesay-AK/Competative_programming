class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        words={}
        for word in list1:
            if word in list2:
                words[word]=list1.index(word)+list2.index(word)
                
        
        The_minimum=min(words.values())
        result=[]
        for word in words:
            if words[word]==The_minimum:
                result.append(word)
        return result

            
                
