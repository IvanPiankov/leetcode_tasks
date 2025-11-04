# Definition for singly-linked list.
from typing import Optional

from Trees.base_tree_node import build_tree_from_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def depth(root: Optional[TreeNode], min_val: float | int, max_val: float | int) -> bool:
            if not root:
                return True

            if not min_val < root.val < max_val:
                return False

            return depth(root.left, min_val=min_val, max_val=root.val) and depth(root.right,  min_val=root.val, max_val=max_val)

        is_valid = depth(root, float('-inf'), float('inf'))

        return is_valid




if __name__ == "__main__":
    # Test 1
    data = [2,1,3]
    root = build_tree_from_list(data)
    level_order = Solution().isValidBST(root)
    print(f"Test 1- {level_order}")
    # Test 2
    data = [5,1,4,None,None,3,6]
    root = build_tree_from_list(data)
    level_order = Solution().isValidBST(root)
    print(f"Test 2- {level_order}")
