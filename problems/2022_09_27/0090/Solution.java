// NU

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        backtrack(0, res, list, nums);
        return res;
    }

    private void backtrack(int index, List<List<Integer>> res, List<Integer> list, int[] nums) {
        res.add(new ArrayList<>(list));

        for (int i = index; i < nums.length; ++i) {
            if (i > index && nums[i] == nums[i - 1]) {
                continue;
            }
            list.add(nums[i]);
            backtrack(i + 1, res, list, nums);
            list.remove(list.size() - 1);
        }
    }
}