class Solution:
    def numberOfPermutations(self, n, requirements):
        MOD = 10**9 + 7
        
        # store requirements
        req = {e: c for e, c in requirements}
        
        max_inv = 400
        
        # dp[k] = ways for previous size
        dp = [0] * (max_inv + 1)
        dp[0] = 1
        
        for size in range(1, n + 1):
            new = [0] * (max_inv + 1)
            
            window_sum = 0  # sliding window sum
            
            for k in range(max_inv + 1):
                
                # add current value
                window_sum += dp[k]
                
                # remove extra (window size > size)
                if k >= size:
                    window_sum -= dp[k - size]
                
                # keep value in range
                window_sum %= MOD
                
                new[k] = window_sum
            
            # apply requirement constraint
            if size - 1 in req:
                need = req[size - 1]
                
                for k in range(max_inv + 1):
                    if k != need:
                        new[k] = 0
            
            dp = new
        
        return sum(dp) % MOD