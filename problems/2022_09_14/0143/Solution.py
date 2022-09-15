# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        reverse = None
        curr = slow.next
        while curr:
            temp = curr.next
            curr.next = reverse
            reverse = curr
            curr = temp
        slow.next = None

        head1, head2 = head, reverse
        while head2:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head1 = next1

            head2.next = head1
            head2 = next2
