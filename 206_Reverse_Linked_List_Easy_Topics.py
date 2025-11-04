# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current is not None:
            next_node = current.next

            current.next = prev

            prev = current
            current = next_node

        return prev

def print_list(node):
    while node is not None:
        print(f" {node.val}", end="")
        node = node.next
    print()


if __name__ == "__main__":
    linked_list = ListNode(1)
    linked_list.next = ListNode(2)

    print_list(linked_list)

    linked_list = Solution().reverseList(linked_list)

    while linked_list is not None:
        print(f" {linked_list.val}", end="")
        linked_list = linked_list.next

    # print()
    # print()

    # timeMap = TimeMap()
    # print(timeMap.set("foo", "bar", 1))
    # print(timeMap.get("foo", 1))
    # print(timeMap.get("foo", 3))
    # print(timeMap.set("foo", "bar2", 4))
    # print(timeMap.get("foo", 4))
    # print(timeMap.get("foo", 5))
