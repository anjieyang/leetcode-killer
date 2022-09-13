/*
 * Author: digmouse233
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for (String token : tokens) {
            if (token.equals("+")) {
                stack.add(stack.pop() + stack.pop());
            } else if (token.equals("*")) {
                stack.add(stack.pop() * stack.pop());
            } else if (token.equals("-")) {
                int secNum = stack.pop();
                int firNum = stack.pop();
                stack.add(firNum - secNum);
            } else if (token.equals("/")) {
                int secNum = stack.pop();
                int firNum = stack.pop();
                stack.add(firNum / secNum);
            } else {
                stack.add(Integer.parseInt(token));
            }
        }

        return stack.peek();
    }
}
