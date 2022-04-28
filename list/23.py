# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heap
        # q = []
        # for i in range(len(lists)):
        #     if(lists[i]):
        #         heapq.heappush(q, (lists[i].val, i)) # heap will sort by first element in tuple
        #         lists[i] = lists[i].next
        # res = ListNode()
        # cur = res
        # while q:
        #     val, i = heapq.heappop(q)
        #     cur.next = ListNode(val)
        #     cur = cur.next
        #     if lists[i]:
        #         heapq.heappush(q, (lists[i].val, i))
        #         lists[i] = lists[i].next
        # return res.next
        
        # Divide And Conquer
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next