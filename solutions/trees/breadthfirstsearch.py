from typing import List

from utils import TreeNode


# noinspection PyMethodMayBeStatic,DuplicatedCode
class Solution:
    # id102 _Tree _BreadthFirstSearch
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

    # id103 _Stack _Tree _BreadthFirstSearch
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

    # id107 _Tree _BreadthFirstSearch
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

    # id111 _Tree _DepthFirstSearch _BreadthFirstSearch
    # Todo: see should dfs?
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

    # id463 _HashTable
    # Todo: see ht
    # Todo: write solution
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return self._islandPerimeter(grid, i, j)

    def _islandPerimeter(self, grid: List[List[int]], i: int, j: int) -> int:
        visited = [[False for _ in row] for row in grid]
        result = 0

        queue = [(i, j)]
        visited[i][j] = True

        while len(queue) != 0:
            x, y = queue.pop(0)

            if -1 < x + 1 < len(grid) and -1 < y < len(grid[0]):
                if grid[x + 1][y] == 0:
                    result += 1
                else:
                    if not visited[x + 1][y]:
                        visited[x + 1][y] = True
                        queue.append((x + 1, y))
            else:
                result += 1

            if -1 < x - 1 < len(grid) and -1 < y < len(grid[0]):
                if grid[x - 1][y] == 0:
                    result += 1
                else:
                    if not visited[x - 1][y]:
                        visited[x - 1][y] = True
                        queue.append((x - 1, y))
            else:
                result += 1

            if -1 < x < len(grid) and -1 < y + 1 < len(grid[0]):
                if grid[x][y + 1] == 0:
                    result += 1
                else:
                    if not visited[x][y + 1]:
                        visited[x][y + 1] = True
                        queue.append((x, y + 1))
            else:
                result += 1

            if -1 < x < len(grid) and -1 < y - 1 < len(grid[0]):
                if grid[x][y - 1] == 0:
                    result += 1
                else:
                    if not visited[x][y - 1]:
                        visited[x][y - 1] = True
                        queue.append((x, y - 1))
            else:
                result += 1

        return result

    # id637 _Tree
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

    # id653 _Tree
    # Todo: see dfs
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
        Start bfs from root
        If pair for value node exists in pairs -> return True
        Otherwise -> add pair for current value
        Also append not None children of node
        If left from while -> return False
        """
        queue, pairs = [root], {}

        while len(queue) != 0:
            node = queue.pop(0)

            if pairs[node.val]:
                return True

            pairs[k - node.val] = True

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return False
