# Last updated: 8/12/2025, 11:45:59 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle = []
    
        for i in range(numRows):
            row = [1] * (i + 1)
            if i > 1:
                prev = triangle[i - 1]
                for j in range(1, i):
                    row[j] = prev[j - 1] + prev[j]
            triangle.append(row)
            
        return triangle

        