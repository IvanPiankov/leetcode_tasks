# Definition for singly-linked list.
from typing import Optional

from Trees.base_tree_node import build_tree_from_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.counter = 0


    def goodNodes(self, root: TreeNode) -> int:
        max_val = root.val

        def depth(root: Optional[TreeNode], max_val: int) -> int:
            if not root:
                return self.counter

            if root.val >= max_val:
                self.counter += 1

            new_max_val = max(max_val, root.val)

            depth(root.left, new_max_val)
            depth(root.right, new_max_val)

            return self.counter

        depth(root, max_val)

        return self.counter




if __name__ == "__main__":
    # Test 1
    data = [3,1,4,3,None,1,5]
    root = build_tree_from_list(data)
    level_order = Solution().goodNodes(root)
    print(f"Test 1- {level_order}")
    # Test 2
    data = [3,3,None,4,2]
    root = build_tree_from_list(data)
    level_order = Solution().goodNodes(root)
    print(f"Test 2- {level_order}")
    # Test 3
    data = [1]
    root = build_tree_from_list(data)
    level_order = Solution().goodNodes(root)
    print(f"Test 3- {level_order}")
    # Test 4
    data = [2,None,4,10,8,None,None,4]
    root = build_tree_from_list(data)
    level_order = Solution().goodNodes(root)
    print(f"Test 4- {level_order}")


