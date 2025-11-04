# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode()

        extra_value = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            extra_value, node_value = divmod(val1 + val2 + extra_value, 10)

            current.next = ListNode(node_value)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if extra_value:
            current.next = ListNode(extra_value)

        return dummy.next


def print_list(node):
    while node is not None:
        print(f" {node.val}", end="")
        node = node.next
    print()


if __name__ == "__main__":
    linked_list = ListNode(2)
    linked_list.next = ListNode(4)
    linked_list.next.next = ListNode(3)

    linked_list2 = ListNode(5)
    linked_list2.next = ListNode(6)
    linked_list2.next.next = ListNode(4)


    print_list(linked_list)

    linked_list = Solution().addTwoNumbers(linked_list, linked_list2)

    while linked_list is not None:
        print(f" {linked_list.val}", end="")
        linked_list = linked_list.next

