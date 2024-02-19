class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = defaultdict(int)
        for i in range(len(nums2)):
            if not stack:
                stack.append(nums2[i])
        
            while stack and stack[-1] < nums2[i]:
                ans[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

       
        for i in range(len(nums1)):
            if ans[nums1[i]]:
                nums1[i] = ans[nums1[i]]
            else:
                nums1[i] = -1
        return nums1