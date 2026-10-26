class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # dp[i] stores the maximum sum for the prefix of length i
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            current_max = 0
            # Look back up to k elements to form the last partition
            for j in range(1, min(k, i) + 1):
                # Track the maximum element in the current partition arr[i-j ... i-1]
                current_max = max(current_max, arr[i - j])
                # Update dp[i] by taking the best partition split
                dp[i] = max(dp[i], dp[i - j] + current_max * j)
                
        return dp[n]