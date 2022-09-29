class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.backtracking(candidates, target, [], 0, 0)
        return self.res

    def backtracking(self, candidates, target, curr, total, index):
        if total == target:
            self.res.append(curr.copy())
            return

        if index >= len(candidates) or total > target:
            return

        curr.append(candidates[index])
        self.backtracking(candidates, target, curr,
                          total + candidates[index], index)

        curr.pop()
        self.backtracking(candidates, target, curr, total, index + 1)
