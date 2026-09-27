# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        curr1=l1
        curr2=l2
        neo=ListNode(0)
        curr3=neo
        while curr1 and curr2:
            summ=curr1.val+curr2.val+carry
            if summ<10:
                curr3.next=ListNode(summ)
                carry=0
            else:
                curr3.next=ListNode(summ%10)
                carry=1
            curr1=curr1.next
            curr2=curr2.next
            curr3=curr3.next
        while curr1:
            summ=curr1.val+carry
            if summ<10:
                curr3.next=ListNode(summ)
                carry=0
            else:    
                curr3.next=ListNode(summ%10)
                carry=1
            curr1=curr1.next
            curr3=curr3.next
        while curr2:
            summ=curr2.val+carry
            if summ<10:
                curr3.next=ListNode(summ)
                carry=0
            else:    
                curr3.next=ListNode(summ%10)
                carry=1
            curr2=curr2.next
            curr3=curr3.next
        if carry:
            curr3.next=ListNode(1)
        return neo.next