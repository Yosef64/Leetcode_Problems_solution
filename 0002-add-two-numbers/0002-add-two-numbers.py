# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1,lst2,l=[],[],[]
        while l1:
            lst1.append(str(l1.val))
            l1 = l1.next
        while l2:
            lst2.append(str(l2.val))
            l2 = l2.next
        con1 , con2 = "".join(lst1) , "".join(lst2)
        total = int(con1[::-1]) + int(con2[::-1])
        final = [int(x) for x in str(total)]
        final.reverse()
        ref = ListNode(final[0])
        head = ref
        for i in range(1,len(final)):
            temp = ListNode(final[i])
            ref.next = temp
            ref = ref.next
        return head
        
        