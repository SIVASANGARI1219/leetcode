class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(start, path, total):
            
            if total == target:          # Base case
                result.append(path)
                return
            
            if total > target:           # Base case
                return
            
            # recursive case
            for i in range(start, len(candidates)):
            # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                dfs(i+1, path + [candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return result