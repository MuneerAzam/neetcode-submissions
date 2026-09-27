"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None
        if not head.next:
            if head.random:
                n=Node(head.val,None,None)
                n.random=n
            else:
                n=Node(head.val,None,None)
            return n
        curr1=head
        neo=Node(head.val,None)
        dict={}
        dict[head]=neo
        curr1=curr1.next
        curr2=neo
        while curr1:
            curr2.next=Node(curr1.val)
            curr2=curr2.next
            dict[curr1]=curr2
            curr1=curr1.next
        curr1=head
        curr2=neo
        while curr1:
            if not curr1.random:
                curr1=curr1.next
                curr2=curr2.next
                continue
            else:
                curr2.random=dict[curr1.random]
            curr1=curr1.next
            curr2=curr2.next
        return neo


