# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return

        slow = fast = head

        # Определить середину связанного списка
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Перевернуть правую часть списка
        prev, current = None, slow

        while current is not None:
            current.next, prev, current = prev, current, current.next

        # Смерджить два листа
        first, second = head, prev
        while second.next:
            next_first = first.next
            next_second = second.next

            first.next = second
            first = next_first

            second.next = first
            second = next_second




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

    linked_list = Solution().reorderList(linked_list)

    while linked_list is not None:
        print(f" {linked_list.val}", end="")
        linked_list = linked_list.next

