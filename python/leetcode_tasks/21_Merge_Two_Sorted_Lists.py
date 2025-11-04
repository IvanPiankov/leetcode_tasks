# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
            else:
                current.next = list2
                list2, current = list2.next, list2

        if list1 or list2:
            current.next = list1 if list1 else list2

        return dummy.next


def print_list(node: ListNode):
    while node is not None:
        print(f" {node.val}", end="")
        node = node.next
    print()


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)

    list2 = ListNode(2)
    list2.next = ListNode(3)

    merged_list = Solution().mergeTwoLists(list1, list2)

    print_list(merged_list)
