class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nameToHeight={}
        for i in range(len(names)):
            nameToHeight[heights[i]]=names[i]
        heights.sort(reverse=True)
        return [nameToHeight[i] for i in heights]
         
        
        
            