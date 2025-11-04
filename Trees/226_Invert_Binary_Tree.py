# Definition for singly-linked list.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        pointer = root.left
        root.left = root.right
        root.right = pointer

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == "__main__":
    pass

