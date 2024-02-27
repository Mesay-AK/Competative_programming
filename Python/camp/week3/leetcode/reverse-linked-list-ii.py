# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        curr = head
        count = 0
        to_be_flipped = []

        while curr:
            if count  >= left-1 and count <= right-1:
                to_be_flipped.append(curr.val)
            count += 1

            curr = curr.next

        curr = head
        count = 0
        i = len(to_be_flipped)-1
        while curr:
            if count  >= left-1 and count <= right-1:
                curr.val = to_be_flipped[i]
                i -= 1
            count += 1

            curr = curr.next

        return head