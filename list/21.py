# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # iterative
        # head = ListNode(0)
        # move=head
        # if not list1: return list2
        # if not list2: return list1
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         move.next = list1
        #         list1 = list1.next
        #     else:
        #         move.next= list2
        #         list2 = list2.next
        #     move = move.next
        # move.next = list1 if list1 else list2
        # return head.next
        
        # recursive
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            node = list1
            node.next = self.mergeTwoLists(list1.next, list2)
        else:
            node = list2
            node.next = self.mergeTwoLists(list1, list2.next)
        return node