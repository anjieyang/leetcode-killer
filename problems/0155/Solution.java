import java.util.Stack;

/*
 * Author: digmouse233
 * Time Complexity:
 * Space Complexity:
 */

public class Solution {
    Stack<Integer> stack;
    Stack<int[]> minStack;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int val) {
        stack.push(val);

        if (minStack.isEmpty() || val < minStack.peek()[0]) {
            minStack.push(new int[] { val, 1 });
        } else if (val == minStack.peek()[0]) {
            minStack.peek()[1]++;
        }
    }

    public void pop() {
        int val = stack.pop();
        if (val == minStack.peek()[0]) {
            minStack.peek()[1]--;
        }
        if (0 == minStack.peek()[1]) {
            minStack.pop();
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek()[0];
    }
}
