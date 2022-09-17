/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    private List<Integer> list = new ArrayList<>();

    public int kthSmallest(TreeNode root, int k) {
        dfs(root);
        Collections.sort(list);
        return list.get(k - 1);
    }

    private void dfs(TreeNode root) {
        if (root == null) {
            return;
        }

        list.add(root.val);

        if (root.left != null) {
            dfs(root.left);
        }

        if (root.right != null) {
            dfs(root.right);
        }
    }
}