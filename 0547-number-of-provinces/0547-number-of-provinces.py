class Solution:
    def findCircleNum(self, c: List[List[int]]) -> int:
        rows,cols = len(c) , len(c[0])
        nodes = [ind for ind in range(rows)]
        def find(cur):
            if cur == nodes[cur]:
                return cur
            return find(nodes[cur])
        def union(n1, n2):
            pn1 , pn2 = find(n1),find(n2)
            nodes[pn1] = pn2
        for row in range(rows):
            for col in range(cols):
                if c[row][col] == 1:
                    union(row,col)
        count = 0
        for ind in range(len(nodes)):
            if ind == nodes[ind]:
                count += 1
        return count
