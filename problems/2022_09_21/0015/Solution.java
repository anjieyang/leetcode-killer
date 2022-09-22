class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();

        Arrays.sort(nums);
        for (int i = 0; i < nums.length && nums[i] <= 0; ++i) {
            if (i == 0 || nums[i] != nums[i - 1]) {
                helper(nums, i, res);
            }
        }

        return res;
    }

    private void helper(int[] nums, int i, List<List<Integer>> res) {
        int j = i + 1, k = nums.length - 1;
        int complement = 0 - nums[i];

        while (j < k) {
            if (nums[j] + nums[k] < complement) {
                j++;
            } else if (nums[j] + nums[k] > complement) {
                k--;
            } else {
                res.add(Arrays.asList(nums[i], nums[j++], nums[k--]));
                while (j < k && nums[j] == nums[j - 1]) {
                    j++;
                }
            }
        }
    }
}