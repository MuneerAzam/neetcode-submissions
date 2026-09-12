# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        nodes=[]
        current=head
        while current!=None:
            if nodes==[]:
                node=ListNode(current.val)
                node.next=None
                nodes.insert(0,node)
                current=current.next
            else:
                node=ListNode(current.val)
                node.next=nodes[0]
                nodes.insert(0,node)
                current=current.next

        return nodes[0]