from typing import List

from utils import TreeNode


# noinspection PyMethodMayBeStatic,DuplicatedCode,PyPep8Naming
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

    # id127 _BreadthFirstSearch
    # Todo: re-read
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict
        matches = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                matches[word[:i] + '!' + word[i + 1:]].append(word)

        used = {beginWord: True}
        level = 1
        queue = [beginWord]

        while queue:
            for _ in range(len(queue)):
                current = queue.pop(0)

                for i in range(len(current)):

                    dummy = current[:i] + '!' + current[i + 1:]

                    for match in matches[dummy]:
                        if match == endWord:
                            return level + 1

                        if match not in used:
                            used[match] = True
                            queue.append(match)

            level += 1

        return 0

    # id130 _DepthFirstSearch _BreadthFirstSearch _UnionFind
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        With dfs function visit all nodes connected with borders (go dfs from borders nodes and mark them as visited)
        Next, for other nodes go dfs and then flip them to X (since all union related with borders already marked
            and not included in current dfs runs)
        """
        if len(board) == 0:
            return

        visited = [[False for _ in row] for row in board]

        for i in range(len(board)):
            if self._solveCheck(i, 0, visited, board):
                self._solve(i, 0, visited, board, False)
            if self._solveCheck(i, len(board[0]) - 1, visited, board):
                self._solve(i, len(board[0]) - 1, visited, board, False)

        for j in range(len(board[0])):
            if self._solveCheck(0, j, visited, board):
                self._solve(0, j, visited, board, False)
            if self._solveCheck(len(board) - 1, j, visited, board):
                self._solve(len(board) - 1, j, visited, board, False)

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if self._solveCheck(i, j, visited, board):
                    self._solve(i, j, visited, board, True)

    def _solve(self, i: int, j: int, visited: List[List[bool]], board: List[List[str]], mode: bool) -> None:
        queue = [(i, j)]
        visited[i][j] = True

        while queue:
            x, y = queue.pop()

            if mode:
                board[x][y] = 'X'

            if self._solveCheckRange(x + 1, y, visited, board):
                self._solve(x + 1, y, visited, board, mode)

            if self._solveCheckRange(x - 1, y, visited, board):
                self._solve(x - 1, y, visited, board, mode)

            if self._solveCheckRange(x, y + 1, visited, board):
                self._solve(x, y + 1, visited, board, mode)

            if self._solveCheckRange(x, y - 1, visited, board):
                self._solve(x, y - 1, visited, board, mode)

    def _solveCheckRange(self, i: int, j: int, visited: List[List[bool]], board: List[List[str]]):
        return -1 < i < len(board) and -1 < j < len(board[0]) and self._solveCheck(i, j, visited, board)

    def _solveCheck(self, i: int, j: int, visited: List[List[bool]], board: List[List[str]]):
        return not visited[i][j] and board[i][j] == 'O'

    # id199 _Tree _DepthFirstSearch _BreadthFirstSearch
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        Init queue for bfs
        For every level of tree (with inner for loop) update value as right_most
        After leaving level -> append to result
        Return result
        """
        from collections import deque

        queue = deque()

        if root:
            queue.append(root)

        result = []

        while queue:
            right_most = -1

            for _ in range(len(queue)):
                node = queue.popleft()

                right_most = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(right_most)

        return result

    # id200 _DepthFirstSearch _BreadthFirstSearch _UnionFind
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Init same size matrix with used (visited) property
        _numIslands mark element as used
        Check all adjacent elements for bounds, used property and value
        If element valid and not used -> call recursion from element
        Iterate over matrix and call recursion function
        Since one outer call of function mark as used whole island, count all calls of outer function
        Return count
        """
        count = 0
        used = [[False for _ in row] for row in grid]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not used[i][j] and grid[i][j] == '1':
                    count += 1
                    self._numIslands(grid, used, i, j)

        return count

    def _numIslands(self, grid: List[List[str]], used: List[List[bool]], i: int, j: int) -> None:
        queue = [(i, j)]
        used[i][j] = True

        while queue:
            x, y = queue.pop(0)

            if self._numIslandsCheck(grid, used, x + 1, y):
                used[x + 1][y] = True
                queue.append((x + 1, y))

            if self._numIslandsCheck(grid, used, x - 1, y):
                used[x - 1][y] = True
                queue.append((x - 1, y))

            if self._numIslandsCheck(grid, used, x, y + 1):
                used[x][y + 1] = True
                queue.append((x, y + 1))

            if self._numIslandsCheck(grid, used, x, y - 1):
                used[x][y - 1] = True
                queue.append((x, y - 1))

    def _numIslandsCheck(self, grid: List[List[str]], used: List[List[bool]], i: int, j: int) -> bool:
        return -1 < i < len(grid) and -1 < j < len(grid[0]) and not used[i][j] and grid[i][j] == '1'

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

    # id542 _DepthFirstSearch _BreadthFirstSearch
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Init result matrix of same size
        Run bfs with returning level of bfs for finding nearest 0 and set element value
        Return result
        """
        return [[self._updateMatrix(matrix, i, j) for j in range(len(matrix[0]))] for i in range(len(matrix))]

    def _updateMatrix(self, matrix: List[List[int]], i: int, j: int) -> int:
        """
        Run bfs until find 0
        Return level (distance) for that 0
        """
        level = 0
        queue = [(i, j)]

        while queue:
            for _ in range(len(queue)):
                x, y = queue.pop(0)

                if matrix[x][y] == 0:
                    return level

                if -1 < x + 1 < len(matrix) and -1 < y < len(matrix[0]):
                    queue.append((x + 1, y))

                if -1 < x - 1 < len(matrix) and -1 < y < len(matrix[0]):
                    queue.append((x - 1, y))

                if -1 < x < len(matrix) and -1 < y + 1 < len(matrix[0]):
                    queue.append((x, y + 1))

                if -1 < x < len(matrix) and -1 < y - 1 < len(matrix[0]):
                    queue.append((x, y - 1))

            level += 1

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

    # id773 _BreadthFirstSearch
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        Save hash of matrix to used
        Go bfs from initial matrix with all possible (not used) transformations
        If current transformation is result -> return moves
        Otherwise -> not possible, return -1
        """
        used = {self._slidingPuzzle(board): True}
        queue = [board]
        result = [[1, 2, 3], [4, 5, 0]]
        moves = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.pop(0)

                if current == result:
                    return moves

                x, y = 0, 0

                for i in range(len(current)):
                    for j in range(len(current[0])):
                        if current[i][j] == 0:
                            x, y = i, j

                pairs = ((1, 0), (-1, 0), (0, 1), (0, -1))

                for pair in pairs:
                    if -1 < x + pair[0] < len(current) and -1 < y + pair[1] < len(current[0]):
                        copy = [[el for el in row] for row in current]
                        copy[x][y], copy[x + pair[0]][y + pair[1]] = copy[x + pair[0]][y + pair[1]], copy[x][y]
                        if not used.get(self._slidingPuzzle(copy)):
                            used[self._slidingPuzzle(copy)] = True
                            queue.append(copy)

            moves += 1

        return -1

    def _slidingPuzzle(self, board: List[List[int]]) -> int:
        return board[0][0] + 31 * board[0][1] + 31 ** 2 * board[0][2] + \
               31 ** 3 * board[1][0] + 31 ** 4 * board[1][1] + 31 ** 5 * board[1][2]
