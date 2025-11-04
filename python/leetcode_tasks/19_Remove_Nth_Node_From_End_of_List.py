# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = dummy = ListNode(0, head)

        for _ in range(n + 1):
            fast = fast.next

        while fast is not None:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next


def print_list(node):
    while node is not None:
        print(f" {node.val}", end="")
        node = node.next
    print()


if __name__ == "__main__":
    linked_list = ListNode(1)
    linked_list.next = ListNode(2)
    linked_list.next.next = ListNode(3)
    linked_list.next.next.next = ListNode(4)
    linked_list.next.next.next.next = ListNode(5)

    print_list(linked_list)

    linked_list = Solution().removeNthFromEnd(linked_list, 5)

    while linked_list is not None:
        print(f" {linked_list.val}", end="")
        linked_list = linked_list.next

