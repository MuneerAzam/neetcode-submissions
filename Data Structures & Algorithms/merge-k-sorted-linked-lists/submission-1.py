import heapq as hq

class Solution:
    def mergeKLists(self, lists):
        q = []
        for i, node in enumerate(lists):
            if node:
                hq.heappush(q, (node.val, i, node))
        dummy = ListNode()
        curr = dummy
        while q:
            val, i, node = hq.heappop(q)
            curr.next = node
            curr = curr.next
            if node.next:
                hq.heappush(q, (node.next.val, i, node.next))
        return dummy.next
