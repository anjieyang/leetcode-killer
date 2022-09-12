// digmouse233

public class Solution {
    public int search(int[] nums, int target) {
        // Initialize two pointers
        int left = 0;
        int right = nums.length;

        // Left pointer will be contained
        // Right pointer will not be contained
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (target == nums[mid]) {
                return mid;
            }

            if (target > nums[mid]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        // Return -1 if there is no target in the array
        return -1;
    }
}