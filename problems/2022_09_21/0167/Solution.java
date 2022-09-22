class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1;

        while (target != numbers[left] + numbers[right]) {
            if (target > numbers[left] + numbers[right]) {
                left++;
            }

            if (target < numbers[left] + numbers[right]) {
                right--;
            }
        }

        return new int[] { left + 1, right + 1 };
    }
}