from typing import List

from utils import TreeNode


# noinspection PyMethodMayBeStatic,DuplicatedCode
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        If root is None -> []
        Prepare for BFS with list as queue
        Start BSF from root
        While queue is not empty:
        Pop all nodes in queue
        Add current nodes to level list (depends on left_to_right)
        For every not None children append to queue
        Append level list to result
        Inverse left_to_right
        Return result
        """
        result = []

        if root is None:
            return result

        queue = [root]
        left_to_right = True

        while len(queue) != 0:
            level = []

            for i in range(len(queue)):
                current = queue.pop(0)

                if left_to_right:
                    level.append(current.val)
                else:
                    level.insert(0, current.val)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

            result.append(level)
            left_to_right = not left_to_right

        return result


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.

        Use list as queue (append, pop(0) methods allowed)
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.

        Append element to queue
        Re-append all popped elements except x
        """
        self.queue.append(x)

        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.

        Use simple list and field for storing min value
        """
        self.stack = []
        self._min = 10000000000000

    def push(self, x: int) -> None:
        """
        If x is less than _min -> override _min
        Push x to stack
        """
        if self._min > x:
            self._min = x

        self.stack.append(x)

    def pop(self) -> None:
        """
        Remove last element
        If last element is _min -> search for new _min in stack
        """
        last = self.stack.pop()

        if self._min == last:
            self._min = 10000000000000

            for num in self.stack:
                self._min = min(self._min, num)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min
