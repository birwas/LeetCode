# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        while prev.next:
            cur=prev.next
            if cur.next and cur.val==cur.next.val:
                while cur.next and cur.val==cur.next.val:
                    cur=cur.next
                prev.next=cur.next
            else:
                prev=prev.next
        return dummy.next