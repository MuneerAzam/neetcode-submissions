# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        ans = res
        while True:
            curr = ans
            for _ in range(k):
                curr = curr.next
                if curr is None:
                    return res.next
            temp = curr.next
            prev = temp
            curr = ans.next
            while curr != temp:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            nxt = ans.next
            ans.next = prev
            ans = nxt