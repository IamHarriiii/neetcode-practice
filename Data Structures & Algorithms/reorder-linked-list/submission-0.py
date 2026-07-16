# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        half_head = slow.next
        slow.next = None

        prev = None
        curr = half_head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        half_head = prev

        first = head
        second = half_head

        while second:

            next1 = first.next
            next2 = second.next
            
            first.next = second
            second.next = next1

            first = next1
            second = next2
