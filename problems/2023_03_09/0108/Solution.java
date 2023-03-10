public class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return _helper(nums, 0, nums.length - 1);
    }

    private TreeNode _helper(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }

        int mid = left + ((right - left) >> 1);
        TreeNode root = new TreeNode(nums[mid]);

        root.left = _helper(nums, left, mid - 1);
        root.right = _helper(nums, mid + 1, right);

        return root;
    }
}