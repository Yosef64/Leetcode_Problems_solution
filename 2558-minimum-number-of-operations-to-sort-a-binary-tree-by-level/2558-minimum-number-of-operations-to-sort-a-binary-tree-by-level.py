# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def calculateSwaps(arr):
            tempArr = [[val,ind] for ind,val in enumerate(arr)]
            sortedArr = sorted(tempArr)
            swaps, ind = 0, 0
            while ind < len(tempArr):
                if sortedArr[ind][1] != ind:
                    swapedInd = sortedArr[ind][1]
                    sortedArr[ind],sortedArr[swapedInd] = sortedArr[swapedInd],sortedArr[ind]
                    swaps += 1
                    continue
                ind += 1
            return swaps
        q , ans = deque([root]), 0
        while q:
            level_mem = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    level_mem.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    level_mem.append(node.right.val)
                    q.append(node.right)
            swaps = calculateSwaps(level_mem)
            # print(swaps)
            ans += swaps
        return ans