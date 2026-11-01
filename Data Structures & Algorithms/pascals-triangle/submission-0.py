class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [0]*numRows
        for row in range(numRows):
            triangle[row] = [0]*(row+1)
        
        for row in range(numRows):
            triangle[row][0] = 1
            triangle[row][-1] = 1
        
        for row in range(1,numRows):
            for i in range(1, len(triangle[row-1])):
                triangle[row][i] = triangle[row-1][i]+triangle[row-1][i-1]
        

        return triangle
            

        