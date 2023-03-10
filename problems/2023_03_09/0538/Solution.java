public class Solution {
    int val = 0;

    public TreeNode convertBST(TreeNode root) {
        _helper(root);
        return root;
    }

    private void _helper(TreeNode root) {
        if (root == null) {
            return;
        }

        _helper(root.right);
        root.val += val;
        val = root.val;
        _helper(root.left);
    }
}