# Definition for singly-linked list.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root and p.val > root.val and q.val > root.val:
           answer_root = self.lowestCommonAncestor(root.right, p, q)
        elif root and p.val < root.val and q.val < root.val:
           answer_root = self.lowestCommonAncestor(root.left, p, q)
        else:
            answer_root = root

        return answer_root



if __name__ == "__main__":
    pass

