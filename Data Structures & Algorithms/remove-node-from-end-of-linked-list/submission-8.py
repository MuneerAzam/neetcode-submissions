# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dumm=ListNode(0,head)
        front=dumm
        back=dumm
        for i in range(n):
            front=front.next
        while front.next:
            front=front.next
            back=back.next
        back.next=back.next.next
        return dumm.next