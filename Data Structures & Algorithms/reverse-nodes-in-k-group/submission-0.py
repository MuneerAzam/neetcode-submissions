# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[None]*(k-1)
        curr=head
        res=ListNode()
        ans=res
        c=0
        while curr:
            c+=1
            if c%k==0:
                ans.next=curr
                curr=curr.next
                ans=ans.next
                t=k-2
                r=ans
                while t>=0:
                    ans.next=l[t]
                    ans=ans.next
                    t-=1
                ans.next=curr
                l=[None]*(k-1)
            else:
                l[(c%k)-1]=curr
                curr=curr.next
        return res.next