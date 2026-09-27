# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        if not head.next.next:
            if n==1:
                head.next=None
                return head
            else:
                head=head.next
                return head
        l=1
        curr=head
        while curr.next:
            curr=curr.next
            l+=1
        t=l-n
        if t==0:
            head=head.next
            return head
        curr=head
        for i in range(t-1):
            curr=curr.next
        if n==1:
            curr.next=None
        else:
            curr.next=curr.next.next
        return head
