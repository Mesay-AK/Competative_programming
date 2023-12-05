class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # create a variable for the maximum number of candy a kid has.
        maximum=max(candies)
        result=[]
        for kids in candies:
            #check whether the sum of the extra candy and the current candy of the ith kid is greater or equal to the maximum
            if kids+extraCandies>=maximum:
                result.append(True)
            else:
                result.append(False)
        return result