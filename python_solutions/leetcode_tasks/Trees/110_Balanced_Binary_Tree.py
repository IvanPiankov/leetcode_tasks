# Definition for singly-linked list.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.is_balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> int:

        def depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left_depth = depth(root.left)
            right_depth = depth(root.right)

            if abs(left_depth - right_depth) > 1:
                self.is_balanced = False

            return 1 + max(left_depth, right_depth)

        return depth(root)




if __name__ == "__main__":
    pass

