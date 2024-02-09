class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * (n + 1)

        # Creating the prefixSum

        for first, last, seats in bookings:
            result[first-1] += seats
            result[last] -= seats
        
        for i in range(1, n):
            result[i] = result[i] + result[i-1]

        return result[:n]