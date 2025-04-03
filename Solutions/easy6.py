from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        middle = length // 2
        current = head
        for _ in range(middle):
            current = current.next
        return current
