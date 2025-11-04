# Definition for a binary tree node.
from collections import deque

from Trees.base_tree_node import build_tree_from_list, TreeNode


class Solution:
    def levelOrder(self, root: list[TreeNode] | None) -> list[list[int]]:
        if not root:
            return []

        result = []

        queue = deque()
        queue.append(root)

        while queue:
            level_result = []

            for _ in range(len(queue)):
                node = queue.popleft()

                level_result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)


            result.append(level_result)

        return result



if __name__ == "__main__":
    # Test 1
    data = [3, 9, 20, None, None, 15, 7]
    root = build_tree_from_list(data)
    level_order = Solution().levelOrder(root)
    print(level_order)
    # Test 2
    data = [1]
    root = build_tree_from_list(data)
    level_order = Solution().levelOrder(root)
    print(level_order)
    # Test 3
    # Test 2
    data = []
    root = build_tree_from_list(data)
    level_order = Solution().levelOrder(root)
    print(level_order)

