# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

from Trees.base_tree_node import build_tree_from_list, TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level_values = []

            for _ in range(len(queue)):
                node = queue.popleft()

                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if level_values:
                result.append(level_values[-1])


        return result






if __name__ == "__main__":
    # # Test 1
    # data = [1,2,3,None,5,None,4]
    # root = build_tree_from_list(data)
    # level_order = Solution().rightSideView(root)
    # print(f"Test 1- {level_order}")
    # # Test 2
    data = [1,2,3,4,None,None,None,5]
    root = build_tree_from_list(data)
    level_order = Solution().rightSideView(root)
    print(f"Test 2- {level_order}")
    # # Test 3
    # data = [1,None,3]
    # root = build_tree_from_list(data)
    # level_order = Solution().rightSideView(root)
    # print(f"Test 3- {level_order}")
    # # Test 4
    # data = []
    # root = build_tree_from_list(data)
    # level_order = Solution().rightSideView(root)
    # print(f"Test 4- {level_order}")

