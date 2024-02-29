class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        result = 0

        for i in range(len(height)):
            depth = 0
            while stack and height[stack[-1]] <= height[i]:
                popd = stack.pop()
                if i - popd > 1:
                    result += ((i - popd-1) * (height[popd]-depth))
                depth = height[popd]
                
            if stack:
                popd = stack[-1]
                if i - popd > 1:
                    result += ((i - popd- 1)* (height[i]-depth))
                depth = height[popd]
                

            stack.append(i)
            

        return result


 