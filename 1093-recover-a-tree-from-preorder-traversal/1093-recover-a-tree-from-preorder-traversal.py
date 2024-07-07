# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, tra: str) -> Optional[TreeNode]:
        word ,w = tra[0] , ['']
        for char in tra[1:]:
            con1 ,con2= char.isnumeric(),word.isnumeric()
            if con1 == con2:
                word += char
            else:
                w.append(word)
                word = char
        w.append(word)
        ls = [[len(w[i]),w[i+1]] for i in range(0,len(w),2)]
        def fn(prev,cur):
            if cur >= len(ls):
                return [None,cur]
            if prev!= -1 and ls[cur][0] <= ls[prev][0]:
                return [None,cur]
            node = TreeNode(ls[cur][1])
            
            nodeLeft , level = fn(cur,cur+1)
            node.left = nodeLeft
            if level < len(ls) and ls[level][0]-1 == ls[cur][0]:
                nodeRight , level = fn(cur,level)
                node.right = nodeRight
                return [node,level]
            return [node,level]
        result = fn(-1,0)
        return result[0]
                