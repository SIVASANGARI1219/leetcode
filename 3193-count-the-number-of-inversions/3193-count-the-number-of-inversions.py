class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
      
        MOD = 10**9 + 7
        
        req = {e: c for e, c in requirements}
        
        max_inv = 400
        dp = [0] * (max_inv + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            new = [0] * (max_inv + 1)
            
            prefix = 0
            for k in range(max_inv + 1):
                prefix = (prefix + dp[k]) % MOD
                if k >= i:
                    prefix = (prefix - dp[k - i]) % MOD
                new[k] = prefix
            
            # apply requirement if exists
            if i - 1 in req:
                c = req[i - 1]
                for k in range(max_inv + 1):
                    new[k] = new[k] if k == c else 0
            
            dp = new
        
        return sum(dp) % MOD