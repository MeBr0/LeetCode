from typing import List

from utils import TreeNode


# id297 _Tree _Design
# Todo: doing
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = {}

        self._serialize(root, 1, result)
        _result = [result[key] for key in sorted(result)]
        return '[' + ','.join(_result) + ']'

    def _serialize(self, node: TreeNode, index: int, result: dict) -> None:
        if node is None:
            result[index] = 'null'
            return

        result[index] = str(node.val)
        self._serialize(node.left, index * 2, result)
        self._serialize(node.right, index * 2 + 1, result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
