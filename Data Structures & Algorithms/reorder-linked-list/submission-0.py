# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p=deque()
        curr=head
        while curr:
            p.append(curr.val)
            curr=curr.next
        n=len(p)
        curr=head
        for i in range(n):
            if i%2==0:
                curr.val=p.popleft()
                curr=curr.next
            else:
                curr.val=p.pop()
                curr=curr.next


            
        