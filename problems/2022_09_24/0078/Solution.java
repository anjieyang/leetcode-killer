class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        backtrack(0, res, list, nums);
        return res;
    }

    private void backtrack(int i, List<List<Integer>> res, List<Integer> list, int[] nums) {
        if (i >= nums.length) {
            res.add(new ArrayList<>(list));
            return;
        }
        // add the element to the list
        list.add(nums[i]);
        backtrack(i + 1, res, list, nums);

        // do not add the element to the list
        list.remove(list.size() - 1);
        backtrack(i + 1, res, list, nums);
    }
}