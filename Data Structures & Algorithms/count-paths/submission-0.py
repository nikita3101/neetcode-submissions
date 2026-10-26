class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        print(dp)
        for i in range(m):
            dp[i][0] = 1
        print(dp)
        j =0
        for j in range(n):
            dp[0][j] = 1
        print(dp)
        for i in range(m):
            for j in range(n):
                if(i!=0 and j !=0):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[m -1][n-1]