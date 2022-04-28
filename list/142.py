# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head: return None
        # visited = set()
        # while head:
        #     if head in visited:
        #         return head
        #     visited.add(head)
        #     head = head.next
        # return None
        slow, fast = head, head
        while fast:
            if not fast.next: return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow: 
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow
        return None