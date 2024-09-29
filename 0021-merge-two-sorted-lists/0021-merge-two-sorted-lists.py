# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        so=ListNode(0,next=None)
        yo=so
        if list1==None and list2:
            return list2
        elif list2==None and list1:
            return list1  
        while list1 and list2:
            if list1.val>list2.val:
                yo.next=list2
                yo=yo.next
                list2=list2.next
                if list2==None:
                    yo.next=list1
            elif list1.val<=list2.val:
                yo.next=list1
                yo=yo.next
                list1=list1.next
                if list1==None:
                    yo.next=list2
                 
        return so.next
            