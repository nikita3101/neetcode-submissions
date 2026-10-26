class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        00 01 02.     20 10 00
        10 11 12  ->  21 11 01
        20 21 22.     22 
        
        '''
        m = len(matrix)
        n = len(matrix[0])
        temp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                print (str(i)+ "," + str(j) + " ->" + str(n - 1-j)+ "," + str(i))
                temp[i][j] = matrix[n-j -1][i]
        print(temp)
        for i in range(m):
            for j in range(n):
                matrix[i][j] = temp[i][j]