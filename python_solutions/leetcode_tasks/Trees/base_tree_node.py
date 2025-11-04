from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"



def build_tree_from_list(vals: list[int | None]) -> TreeNode | None:
    """
    Построение двоичного дерева по списку значений в порядке level-order.
    None означает отсутствие узла.
    """
    if not vals:
        return None

    it = iter(vals)
    root_val = next(it)
    if root_val is None:
        return None

    root = TreeNode(root_val)
    queue = deque([root])

    for val in it:
        parent = queue[0]  # текущий родитель
        # создаём левый потомок, если ещё нет
        if parent.left is None:
            if val is not None:
                parent.left = TreeNode(val)
                queue.append(parent.left)
        # иначе — правый потомок
        elif parent.right is None:
            if val is not None:
                parent.right = TreeNode(val)
                queue.append(parent.right)
            # оба потомка заполнены — снимаем из очереди
            queue.popleft()

    return root