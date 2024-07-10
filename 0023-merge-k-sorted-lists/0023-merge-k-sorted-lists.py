# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap , length = [] , 0
        heapq.heapify(heap)

        for node in lists:
            while node:
                length += 1
                heapq.heappush(heap,node.val)
                node = node.next
        finalNode = ListNode(0)

        finalRef = finalNode
        for _ in range(length):
            curNode = ListNode(heapq.heappop(heap))
            finalRef.next = curNode
            finalRef = finalRef.next
        return finalNode.next
        
        
