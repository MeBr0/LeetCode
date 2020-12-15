from typing import List

from utils import TreeNode


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    # id20 _String _Stack
    def isValid(self, s: str) -> bool:
        """
        Create pair of parentheses in dict
        If it is opening item -> append to stack
        If it is closing item -> check last element for matching with dict
        If matching -> remove last element, else -> not valid
        """
        stack = []

        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for ch in s:
            if ch in parentheses:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                if parentheses.get(stack[-1]) != ch:
                    return False

                stack.pop()

        return len(stack) == 0

    # id71 _String _Stack
    def simplifyPath(self, path: str) -> str:
        """
        Split path with /
        For every word in split path:
        If empty string or dot (current directory) -> do nothing
        If word is two dots -> exit last directory (if not root)
        Otherwise -> append new directory name to stack (i.e. enter it)
        Return path beginning with /
        """
        stack = []

        for word in path.split('/'):
            if word == '' or word == '.':
                continue
            elif word == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(word)

        return '/' + '/'.join(stack)

    # id84 _Array _Stack
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left, right = [0 for _ in heights], [0 for _ in heights]

        for k in range(len(heights)):
            if len(stack) == 0:
                left[k] = -1
            elif stack[-1][0] < heights[k]:
                left[k] = stack[-1][1]
            else:
                while len(stack) > 0 and stack[-1][0] >= heights[k]:
                    stack.pop()

                if len(stack) == 0:
                    left[k] = -1
                else:
                    left[k] = stack[-1][1]

            stack.append((heights[k], k))

        stack.clear()

        for k in range(len(heights) - 1, -1, -1):
            if len(stack) == 0:
                right[k] = len(heights)
            elif stack[-1][0] < heights[k]:
                right[k] = stack[-1][1]
            else:
                while len(stack) > 0 and stack[-1][0] >= heights[k]:
                    stack.pop()

                if len(stack) == 0:
                    right[k] = len(heights)
                else:
                    right[k] = stack[-1][1]

            stack.append((heights[k], k))

        area = 0

        for k in range(len(heights)):
            area = max(area, (right[k] - left[k] - 1) * heights[k])

        return area

    # id85 _Array _HashTable _DynamicProgramming _Stack
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        heights = [0 for _ in matrix[0]]

        def max_rectangle(heights: List[int]) -> int:
            stack = []
            left, right = [0 for _ in heights], [0 for _ in heights]

            for k in range(len(heights)):
                if len(stack) == 0:
                    left[k] = -1
                elif stack[-1][0] < heights[k]:
                    left[k] = stack[-1][1]
                else:
                    while len(stack) > 0 and stack[-1][0] >= heights[k]:
                        stack.pop()

                    if len(stack) == 0:
                        left[k] = -1
                    else:
                        left[k] = stack[-1][1]

                stack.append((heights[k], k))

            stack.clear()

            for k in range(len(heights) - 1, -1, -1):
                if len(stack) == 0:
                    right[k] = len(heights)
                elif stack[-1][0] < heights[k]:
                    right[k] = stack[-1][1]
                else:
                    while len(stack) > 0 and stack[-1][0] >= heights[k]:
                        stack.pop()

                    if len(stack) == 0:
                        right[k] = len(heights)
                    else:
                        right[k] = stack[-1][1]

                stack.append((heights[k], k))

            area = 0

            for k in range(len(heights)):
                area = max(area, (right[k] - left[k] - 1) * heights[k])

            return area

        result = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            result = max(result, max_rectangle(heights))

        return result

    # id94 _HastTable _Stack _Tree
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Create list for results and stack for ordering traversal and counting appearance (first or not)
        Begin from root (False - first appearance)
        While stack not empty:
        Pop last element
        If elements not first appearance -> append node value to result
        Otherwise ->
            Append right child as first appearance (if not None)
            Append current node to stack as second appearance
            Append left child as first appearance (if not None) (i.e. right children must be last ones)
        Return result
        """
        result = []

        if root is None:
            return []

        stack = [(root, False)]

        while stack:
            current = stack.pop()

            node = current[0]

            if current[1]:
                result.append(node.val)
                continue

            if node.right is not None:
                stack.append((node.right, False))

            stack.append((node, True))

            if node.left is not None:
                stack.append((node.left, False))

        return result

    # id144 _Stack _Tree
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Create list for results and stack for ordering traversal
        Begin from root
        While stack not empty:
        Pop last element
        Append its value to result
        Append right child (if not None)
        Append left child (if not None) (i.e. right children must be last ones)
        Return result
        """
        result = []

        if root is None:
            return []

        stack = [root]

        while stack:
            current = stack.pop()

            result.append(current.val)

            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

        return result

    # id145 _Stack _Tree
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Create list for results and stack for ordering traversal and counting appearance (first or not)
        Begin from root (False - first appearance)
        While stack not empty:
        Pop last element
        If elements not first appearance -> append node value to result
        Otherwise ->
            Append current node to stack as second appearance
            Append right child as first appearance (if not None)
            Append left child as first appearance (if not None) (i.e. nodes itself must be last ones)
        Return result
        """
        result = []

        if root is None:
            return []

        stack = [(root, False)]

        while stack:
            current = stack.pop()

            node = current[0]

            if current[1]:
                result.append(node.val)
                continue

            stack.append((node, True))

            if node.right is not None:
                stack.append((node.right, False))

            if node.left is not None:
                stack.append((node.left, False))

        return result

    # id150 _Stack
    # Todo: too slow
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Create stack for numbers
        If string is numeric (handle negatives) -> append to stack
        Otherwise -> pop last two numbers and perform current operation
        (In case of division -> truncate to zero)
        Return last (single) element in stack (i.e. result)
        """
        stack = []

        for token in tokens:
            copy = token[:]
            if copy.lstrip('-').isnumeric():
                stack.append(int(token))
            else:
                if token == '+':
                    second = stack.pop()
                    first = stack.pop()

                    stack.append(first + second)
                elif token == '-':
                    second = stack.pop()
                    first = stack.pop()

                    stack.append(first - second)
                elif token == '*':
                    second = stack.pop()
                    first = stack.pop()

                    stack.append(first * second)
                elif token == '/':
                    import math
                    second = stack.pop()
                    first = stack.pop()

                    stack.append(math.trunc(first / second))

        return int(stack.pop())

    # id735 _Stack
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def add(x: int) -> None:
            if len(stack) == 0:
                stack.append(x)
            else:
                if x > 0:
                    stack.append(x)
                else:
                    if stack[-1] > 0:
                        last = stack.pop()

                        if last > -x:
                            add(last)
                        elif -x > last:
                            add(x)

                    else:
                        stack.append(x)

        for asteroid in asteroids:
            add(asteroid)

        return stack

    # id848 _TwoPointers _Stack
    # Todo: see tp
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
        Append each character in string to stack:
        If # found -> pop last character (backspace it)
        Return whether both strings equal
        """
        return self._backspaceCompare(S) == self._backspaceCompare(T)

    def _backspaceCompare(self, string: str):
        stack = []

        for char in string:
            if char == '#':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
