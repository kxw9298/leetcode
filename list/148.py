# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))
    def merge(self, h1, h2):
        dummy = tail = ListNode()
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
        tail.next = h1 or h2
        return dummy.next
    # def merge(self, l1, l2):
    #     head = ListNode(0)
    #     move = head
    #     if not l1: return l2
    #     if not l2: return l1
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             move.next = l1
    #             l1 = l1.next
    #         else:
    #             move.next = l2
    #             l2 = l2.next
    #         move = move.next
    #     move.next = l1 if l1 else l2
    #     return head.next