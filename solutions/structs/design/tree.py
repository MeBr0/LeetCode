from utils import TreeNode


# id297
# noinspection PyMethodMayBeStatic
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        Do bfs from root
        For every node in queue:
        If node is not None -> append current value to result and append children to queue
        Otherwise -> append null value to result
        Return comma joined string from result list
        """
        result = []

        queue = [root]

        while queue:
            node = queue.pop(0)

            if node:
                result.append(str(node.val))

                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')

        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        Split node values from data split by comma
        Create root node with very first element (or set it to None)
        Add root to queue and do bfs
        For every node in queue:
        If node is not None ->
            Pop next (i incremented) element from values
            Create from it node (or None) and link with current as left child
            Append left child to queue

            Do same with next value and link as right child
            Always check for i index out of range
        Return original root
        """
        values = data.split(',')
        i = 1

        root = TreeNode(values[0]) if values[0] != 'null' else None
        queue = [root]

        while queue:
            node = queue.pop(0)

            if node is not None:
                left = TreeNode(values[i]) if i < len(values) and values[i] != 'null' else None
                node.left = left
                queue.append(left)
                i += 1

                right = TreeNode(values[i]) if i < len(values) and values[i] != 'null' else None
                node.right = right
                queue.append(right)
                i += 1

        return root
