# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseLinked(node1,node2):
            if node1 == None:
                return node2
            if node2 ==None:
                return node1
            if node1.val<node2.val:
                node1.next = reverseLinked(node1.next,node2)
                return node1
            else:
                node2.next = reverseLinked(node1,node2.next)
                return node2
        return reverseLinked(list1,list2)