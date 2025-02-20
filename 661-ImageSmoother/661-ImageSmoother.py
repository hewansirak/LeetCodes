class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        ansMatrix = [[0] * cols for _ in range(rows)] 

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols 

        def getResult(r, c):
            total_sum = 0
            count = 0
            for i in range(max(0, r - 1), min(rows, r + 2)):  
                for j in range(max(0, c - 1), min(cols, c + 2)):
                    total_sum += img[i][j]
                    count += 1
            return total_sum // count  

        for r in range(rows):
            for c in range(cols):
                ansMatrix[r][c] = getResult(r, c)

        return ansMatrix
        