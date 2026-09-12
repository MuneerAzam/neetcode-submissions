# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[]
        if list1==None:
            return list2
        if list2==None:
            return list1
        while list1!=None or list2!=None:
            if list1==None:
                nodes[-1].next=list2
                return nodes[0]
            if list2==None:
                nodes[-1].next=list1
                return nodes[0]
            if list1.val<=list2.val:
                if nodes==[]:
                    node=ListNode(list1.val)
                    node.next=None
                    nodes.append(node)
                    list1=list1.next
                else:
                    node=ListNode(list1.val)
                    nodes[-1].next=node
                    nodes.append(node)
                    list1=list1.next
            else:
                if nodes==[]:
                    node=ListNode(list2.val)
                    node.next=None
                    nodes.append(node)
                    list2=list2.next
                else:
                    node=ListNode(list2.val)
                    nodes[-1].next=node
                    nodes.append(node)
                    list2=list2.next
        return nodes[0]
                
