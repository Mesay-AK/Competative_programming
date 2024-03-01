class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        
        def predict(left, right):
        
            if left > right:
                return 0, 0

            first, f_next = predict(left + 1, right)
            second, s_next = predict(left, right - 1)

            if f_next + nums[left] > s_next + nums[right]:
                temp = f_next + nums[left]
                return temp, first

            else:
                temp = s_next + nums[right]
                return temp, second

        first, second = predict(0, len(nums)-1)

        return first >= second


                        
