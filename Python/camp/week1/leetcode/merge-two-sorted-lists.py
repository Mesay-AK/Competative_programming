# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)

        first = list1
        second = list2
         
        def compare(main, first, second):
            curr = main
            if not first:
                curr.next = second
                return curr

            elif not second:
                curr.next = first
                return curr

            if first.val < second.val:
                curr.next = first
                temp = first.next
                first.next = None
                first = temp

            else:
                curr.next = second
                temp = second.next
                second.next = None
                second = temp

            return compare(curr.next, first, second)
        compare(dummy, first, second)

        return dummy.next