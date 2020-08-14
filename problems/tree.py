from typing import List

from utils import TreeNode


# noinspection PyMethodMayBeStatic,DuplicatedCode
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        If both nodes are None -> True
        If only one of them is None -> False
        If values are equal -> see same for left and right children
        """
        if p is None:
            return q is None
        else:
            if q is None:
                return False
            else:
                return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        """
        If root is None -> True
        Go recursion for two children
        If both are None -> True
        If one of them is None -> False
        If values mot matching -> False
        Go recursion for two children...
        """
        if root is None:
            return True

        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None or right is None:
            return left == right

        if left.val != right.val:
            return False

        return self._isSymmetric(left.right, right.left) and self._isSymmetric(left.left, right.right)

    def maxDepth(self, root: TreeNode) -> int:
        """
        If node is None -> 0
        Otherwise -> incremented maximum of children depth
        """
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    int_max = 10000000000

    def isBalanced(self, root: TreeNode) -> bool:
        """
        If node is None -> 0
        Compare depth of children subtrees
        If difference more than 1 or both or them have unbalanced children subtrees -> int_max
        Otherwise -> maximum depth
        :int_max is value of depth for unbalanced subtree
        """
        return self._isBalanced(root) != self.int_max

    def _isBalanced(self, node: TreeNode) -> int:
        if node is None:
            return 0

        left = self._isBalanced(node.left)
        right = self._isBalanced(node.right)

        print(left, right)

        if abs(left - right) > 1 or left == self.int_max and right == self.int_max:
            return self.int_max

        return max(left, right) + 1

    def minDepth(self, root: TreeNode) -> int:
        """
        If root is None -> 0
        Prepare for BFS with list as queue and levelling
        Start BSF from root
        While queue is not empty:
        Pop all nodes in queue
        If it is leaf -> level (i.e. minimum found)
        For every not None children append to queue
        Increment level
        If function did not return value in cycle -> level
        """
        if root is None:
            return 0

        queue = [root]
        level = 1

        while len(queue) != 0:
            for i in range(len(queue)):
                current = queue.pop(0)

                if current.left is None and current.right is None:
                    return level

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

            level += 1

        return level

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        If root is None -> []
        Prepare for BFS with list as queue
        Start BSF from root
        While queue is not empty:
        Pop all nodes in queue
        Add current nodes to level list
        For every not None children append to queue
        Append level list to result
        Return result
        """
        result = []

        if root is None:
            return result

        queue = [root]

        while len(queue) != 0:
            level = []

            for i in range(len(queue)):
                current = queue.pop(0)

                level.append(current.val)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

            result.append(level)

        return result

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        If root is None -> []
        Prepare for BFS with list as queue
        Start BSF from root
        While queue is not empty:
        Pop all nodes in queue
        Add current nodes to level list
        For every not None children append to queue
        Insert level list to the start of result
        Return result
        """
        result = []

        if root is None:
            return result

        queue = [root]

        while len(queue) != 0:
            level = []

            for i in range(len(queue)):
                current = queue.pop(0)

                level.append(current.val)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

            result.insert(0, level)

        return result

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        If root is None -> []
        Prepare for BFS with list as queue
        Start BSF from root
        While queue is not empty:
        Pop all nodes in queue
        Count sum of all values in nodes
        For every not None children append to queue
        Append average to result
        Return result
        """
        result = []

        if root is None:
            return result

        queue = [root]

        while len(queue) != 0:
            _sum = 0
            size = len(queue)

            for i in range(size):
                current = queue.pop(0)

                _sum += current.val

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

            result.append(_sum / size)

        return result

    def isValidBST(self, root: TreeNode) -> bool:
        """
        For root set interval as huge negative and positive numbers
        For every node:
        If node is None -> True
        If node value within given interval (_min, _max) -> recursion for left and right nodes with new intervals
        Otherwise -> False
        """
        return self._isValidBST(root, -10000000000, 10000000000)

    def _isValidBST(self, node: TreeNode, _min: int, _max: int) -> bool:
        if node is None:
            return True

        if _min < node.val < _max:
            return self._isValidBST(node.left, _min, node.val) and self._isValidBST(node.right, node.val, _max)

        return False

    def findMode(self, root: TreeNode) -> List[int]:
        """
        If root is None -> []
        Create count dict for counting each element (incrementing)
        With DFS count all element in tree
        Retrieve mode as maximum value (frequency) in count
        Iterate over count
        If value is equal to mode -> append to result
        Return result
        """
        result = []

        if root is None:
            return result

        count = self._findMode(root, {})
        mode = max(count.values())

        for value, frequency in count.items():
            if frequency == mode:
                result.append(value)

        return result

    def _findMode(self, node: TreeNode, count: dict) -> dict:
        if node is not None:
            count[node.val] = count.get(node.val, 0) + 1
            self._findMode(node.left, count)
            self._findMode(node.right, count)

        return count
