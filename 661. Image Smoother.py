class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])
        result = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                total, count = 0, 0

                for x in range(max(0, i-1), min(row, i+2)):
                    for y in range(max(0, j-1), min(col, j+2)):
                        total += img[x][y]
                        count += 1

                result[i][j] = total // count

        return result
