class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        backtrack(0, target, candidates, res, list);
        return res;
    }

    private void backtrack(int i, int target, int[] candidates, List<List<Integer>> res, List<Integer> list) {
        if (target == 0) {
            res.add(new ArrayList<>(list));
        } else if (target < 0 || i >= candidates.length) {
            return;
        } else {
            list.add(candidates[i]);
            backtrack(i, target - candidates[i], candidates, res, list);

            list.remove(list.size() - 1);
            backtrack(i + 1, target, candidates, res, list);
        }
    }
}