# Definition for singly-linked list.
from typing import Optional

from Trees.base_tree_node import build_tree_from_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    counter = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def depth(root: Optional[TreeNode]) -> TreeNode | None:
            if not root:
                return None

            left_result = depth(root.left)

            if left_result:
                return left_result

            self.counter +=1

            if self.counter == k:
                return root

            return depth(root.right)

        result = depth(root)

        return result.val if result else 0




if __name__ == "__main__":
    # Test 1
    data = [3,1,4,None,2]
    root = build_tree_from_list(data)
    level_order = Solution().kthSmallest(root, 1)
    print(f"Test 1- {level_order}")
    # Test 2
    data = [5,3,6,2,4,None,None,1]
    root = build_tree_from_list(data)
    level_order = Solution().kthSmallest(root, 3)
    print(f"Test 2- {level_order}")
