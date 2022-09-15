/*
 * Author:
 * Time Complexity:
 * Space Complexity:
 */

public class Solution {
    public void reorderList(ListNode head) {
        if (head == null) {
            return;
        }

        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode prev = null, curr = slow;
        while (curr != null) {
            ListNode tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }

        ListNode first = head, second = prev;
        while (second.next != null) {
            ListNode tmp = first.next;
            first.next = second;
            first = tmp;

            tmp = second.next;
            second.next = first;
            second = tmp;
        }
        
    }
}

        
        