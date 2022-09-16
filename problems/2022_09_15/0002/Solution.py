# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rtn = ListNode(-1)
        curr = rtn

        carryOver = 0
        while l1 and l2:
            add = (l1.val + l2.val + carryOver) % 10
            carryOver = (l1.val + l2.val + carryOver) // 10
            curr.next = ListNode(add)
            curr = curr.next
            l1, l2 = l1.next, l2.next

        while l1:
            add = (l1.val + carryOver) % 10
            carryOver = (l1.val + carryOver) // 10
            curr.next = ListNode(add)
            curr = curr.next
            l1 = l1.next
        while l2:
            add = (l2.val + carryOver) % 10
            carryOver = (l2.val + carryOver) // 10
            curr.next = ListNode(add)
            curr = curr.next
            l2 = l2.next
        if carryOver:
            curr.next = ListNode(carryOver)

        return rtn.next
