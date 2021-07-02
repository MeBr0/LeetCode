class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Node of binary tree
        """
        self.val = val
        self.left = left
        self.right = right


# noinspection PyShadowingBuiltins
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class NAryNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class NNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
