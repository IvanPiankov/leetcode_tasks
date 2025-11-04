# Definition for singly-linked list.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left_length = height(root.left)
            right_length = height(root.right)

            current_diameter = left_length + right_length

            self.diameter = max(current_diameter, self.diameter)

            return 1 + max(left_length, right_length)

        return height(root)




if __name__ == "__main__":
    pass

