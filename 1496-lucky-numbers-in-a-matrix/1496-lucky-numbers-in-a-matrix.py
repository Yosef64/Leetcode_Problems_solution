class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row,col = len(matrix), len(matrix[0])
        eleCol , ans = defaultdict(int) , []
        for r in range(row):
            for c in range(col):
                eleCol[c] = max(matrix[r][c],eleCol[c])
        
        for r in range(row):
            minEle = 0
            for c in range(1,col):
                if matrix[r][c] < matrix[r][minEle]:
                    minEle = c
            if matrix[r][minEle] == eleCol[minEle]:
                ans.append(eleCol[minEle])
        return ans

                
