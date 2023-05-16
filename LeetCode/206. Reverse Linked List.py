# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        curr = head

        while curr:
          curr_next = curr.next
          curr.next = new_head
          new_head = curr
          curr = curr_next
        
        return new_head
