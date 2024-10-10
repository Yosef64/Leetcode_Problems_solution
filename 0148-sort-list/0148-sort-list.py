# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        if head == None:
            return head
        while head:
            lst.append(head.val)
            head = head.next
        lst.sort()
        n1 = ListNode(lst[0])
        head = n1
        for i in range(1,len(lst)):
            node =ListNode(lst[i])
            n1.next = node
            n1 = n1.next
        return head
            
        