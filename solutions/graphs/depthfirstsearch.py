from typing import List

from utils import TreeNode, Node


# noinspection PyShadowingBuiltins,PyPep8Naming,PyMethodMayBeStatic,PyTypeChecker
class Solution:
    # id94 _HashTable _Stack _Tree
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self._inorderTraversal(root)

    def _inorderTraversal(self, node: TreeNode) -> List[int]:
        if node is None:
            return []

        order.extend(self._inorderTraversal(node.left))
        order.append(node.val)
        order.extend(self._inorderTraversal(node.right))

        return order

    # id98 _Tree _DepthFirstSearch
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

    # id100 _Tree _DepthFirstSearch
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

    # id101 _Tree _DepthFirstSearch _BreadthFirstSearch
    # Todo: see bfs
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

    # id104 _Tree _DepthFirstSearch
    def maxDepth(self, root: TreeNode) -> int:
        """
        If node is None -> 0
        Otherwise -> incremented maximum of children depth
        """
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # id105 _Array _Tree _DepthFirstSearch
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Create dict with indices of element in preorder (first) and inorder (second)
        Return root node from whole list preorder
        """
        from collections import defaultdict
        indices = {}
        indices = defaultdict(lambda: [-1, -1], indices)

        for i in range(len(preorder)):
            indices[preorder[i]][0] = i
            indices[inorder[i]][1] = i

        def node_from_preorder(p_i: int, p_j: int) -> TreeNode:
            """
            p_i and p_j is left and right bounds for preorder list
            If bounds not valid (list not empty) -> return null
            Create node from left element in preorder
            With binary search search for first element which index in inorder is greater than node's
            Link node created with bounds p_i + 1 (miss first element) and left as left child
            Link node created with bound left and p_j as right child
            Return node
            """
            if p_i >= p_j:
                return None

            node = TreeNode(preorder[p_i])

            left, right = p_i + 1, p_j - 1

            while left <= right:
                mid = (left + right) // 2

                if indices[preorder[mid]][1] > indices[node.val][1]:
                    right = mid - 1
                else:
                    left = mid + 1

            node.left = node_from_preorder(p_i + 1, left)
            node.right = node_from_preorder(left, p_j)

            return node

        return node_from_preorder(0, len(preorder))

    # id108 _Tree _DepthFirstSearch
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        Return root create from nums list
        """
        def node_from_sorted(left: int, right: int) -> TreeNode:
            """
            If bounds not valid -> return null
            Find middle element and create node from it
            Link node created with left half as left child
            Link node create with right half as right child
            Return node
            """
            if left > right:
                return None

            mid = (left + right) // 2

            node = TreeNode(nums[mid])

            node.left = node_from_sorted(left, mid - 1)
            node.right = node_from_sorted(mid + 1, right)

            return node

        return node_from_sorted(0, len(nums) - 1)

    int_max = 10000000000

    # id110 _Tree _DepthFirstSearch
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

        if abs(left - right) > 1 or left == self.int_max and right == self.int_max:
            return self.int_max

        return max(left, right) + 1

    # id112 _Tree _DepthFirstSearch
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        Go recursive from root with current value 0:
        If node is None -> False
        If current (saved sum) + node.val == sum and node is leaf -> True
        Otherwise check children with updated current value (add node.val)
        """
        return self._hasPathSum(root, sum, 0)

    def _hasPathSum(self, node: TreeNode, _sum: int, current: int) -> bool:
        if node is None:
            return False

        new_value = current + node.val

        if new_value == _sum and node.left is None and node.right is None:
            return True

        return self._hasPathSum(node.left, _sum, new_value) or self._hasPathSum(node.right, _sum, new_value)

    # id113 _Tree _DepthFirstSearch
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        Go recursive from root with current value 0 and empty path list:
        If node is None -> []
        If current (saved sum) + node.val == sum and node is leaf ->
            list wrapped full path (create copy of path and append value)
        Otherwise -> append value to path and gather results from children
        Delete value from path
        Return merged results of two children
        """
        return self._pathSum(root, sum, 0, [])

    def _pathSum(self, node: TreeNode, _sum: int, current: int, path: List[int]) -> List[List[int]]:
        if node is None:
            return []

        new_value = current + node.val

        if new_value == _sum and node.left is None and node.right is None:
            result = path[:]
            result.append(node.val)
            return [result]

        path.append(node.val)

        left_result = self._pathSum(node.left, _sum, new_value, path)
        right_result = self._pathSum(node.right, _sum, new_value, path)

        path.pop()

        left_result.extend(right_result)

        return left_result

    # id116 _Tree _DepthFirstSearch
    def connect(self, root: 'Node') -> 'Node':
        """
        Index of root is 1
        Return mutated root
        """
        self._connect(root, 1, {})

        return root

    def _connect(self, node: 'Node', index: int, nodes: dict):
        """
        If node is child of leaf -> return
        Start from right nodes (index 2 * x + 1, like heap)
        If current index not right most node (check by index is not 2 ** n - 1) -> link next with next node in nodes
        Register node in nodes with index
        End with left nodes (index 2 * x, like heap)
        """
        if node is None:
            return

        self._connect(node.right, index * 2 + 1, nodes)

        if not self._connectDegree(index):
            node.next = nodes[index + 1]

        nodes[index] = node

        self._connect(node.left, index * 2, nodes)

    def _connectDegree(self, index: int) -> bool:
        """
        Check whether index matches formula 2 ** n - 1
        """
        index += 1

        while index != 1:
            if index % 2 == 0:
                index //= 2
            else:
                return False

        return True

    # id124 _Tree _DepthFirstSearch
    # Todo: think about class field, not list
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Create list with single value (target) to pass recursively
        Go recursive from root with minimum int value in num:
        If node is None -> 0
        If results from children is negative -> zero them
        If sum of values of children and root itself gives greater value -> override num
        Return max value of children + node value
        Return updated num
        """
        num = [-999999999999999]

        self._maxPathSum(root, num)

        return num[0]

    def _maxPathSum(self, node: TreeNode, num: List[int]):
        if node is None:
            return 0

        left_result = max(self._maxPathSum(node.left, num), 0)
        right_result = max(self._maxPathSum(node.right, num), 0)
        num[0] = max(num[0], left_result + right_result + node.val)

        return node.val + max(left_result, right_result)

    # id129 _Tree _DepthFirstSearch
    def sumNumbers(self, root: TreeNode) -> int:
        """
        Go recursive from root with empty path list:
        If node is None -> 0
        If node is leaf -> number constructed from digits in path
        Otherwise -> append value to path and gather results from children
        Delete value from path
        Return sum of results of two children
        """
        return self._sumNumbers(root, [])

    def _sumNumbers(self, node: TreeNode, path: List[int]) -> int:
        if node is None:
            return 0

        if node.left is None and node.right is None:
            dummy = path[:]
            dummy.append(node.val)

            num = 0
            for value in dummy:
                num = 10 * num + value

            return num

        path.append(node.val)

        left_result = self._sumNumbers(node.left, path)
        right_result = self._sumNumbers(node.right, path)

        path.pop()

        return left_result + right_result

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
        visited[i][j] = True

        if mode:
            board[i][j] = 'X'

        if self._solveCheckRange(i + 1, j, visited, board):
            self._solve(i + 1, j, visited, board, mode)

        if self._solveCheckRange(i - 1, j, visited, board):
            self._solve(i - 1, j, visited, board, mode)

        if self._solveCheckRange(i, j + 1, visited, board):
            self._solve(i, j + 1, visited, board, mode)

        if self._solveCheckRange(i, j - 1, visited, board):
            self._solve(i, j - 1, visited, board, mode)

    def _solveCheckRange(self, i: int, j: int, visited: List[List[bool]], board: List[List[str]]):
        return -1 < i < len(board) and -1 < j < len(board[0]) and self._solveCheck(i, j, visited, board)

    def _solveCheck(self, i: int, j: int, visited: List[List[bool]], board: List[List[str]]):
        return not visited[i][j] and board[i][j] == 'O'

    # id144 _Stack _Tree
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self._preorderTraversal(root)

    def _preorderTraversal(self, node: TreeNode) -> List[int]:
        if node is None:
            return []

        order = [node.val]
        order.extend(self._preorderTraversal(node.left))
        order.extend(self._preorderTraversal(node.right))

        return order

    # id145 _Stack _Tree
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self._postorderTraversal(root)

    def _postorderTraversal(self, node: TreeNode) -> List[int]:
        if node is None:
            return []

        order = []

        order.extend(self._postorderTraversal(node.left))
        order.extend(self._postorderTraversal(node.right))
        order.append(node.val)

        return order

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
        used[i][j] = True

        if self._numIslandsCheck(grid, used, i + 1, j):
            self._numIslands(grid, used, i + 1, j)

        if self._numIslandsCheck(grid, used, i - 1, j):
            self._numIslands(grid, used, i - 1, j)

        if self._numIslandsCheck(grid, used, i, j + 1):
            self._numIslands(grid, used, i, j + 1)

        if self._numIslandsCheck(grid, used, i, j - 1):
            self._numIslands(grid, used, i, j - 1)

    def _numIslandsCheck(self, grid: List[List[str]], used: List[List[bool]], i: int, j: int) -> bool:
        return -1 < i < len(grid) and -1 < j < len(grid[0]) and not used[i][j] and grid[i][j] == '1'

    # id207 _DepthFirstSearch _BreadthFirstSearch _Graph _TopologicalSort
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Create for each node visited list (0 not visited, 1 visiting, 2 visited)
        Transform edge list prerequisites to adjacency list
        Iterate over courses:
        If node not visited ->
            If dfs function return False (there is cycle) -> return False
        If no cycle found -> return True
        """
        visited = [0 for _ in range(numCourses)]
        adjacency_list = [[] for _ in range(10002)]

        for edge in prerequisites:
            adjacency_list[edge[0]].append(edge[1])

        for i in range(numCourses):
            if visited[i] == 0:
                if not self._canFinish(numCourses, adjacency_list, visited, i):
                    return False

        return True

    def _canFinish(self, numCourses: int, adjacency_list: List[List[int]], visited: List[int], current: int) -> bool:
        """
        Mark node as visiting
        For every node which adjacent to current one:
        If node is visiting (there is cycle) -> return False
        Elif node not visited ->
            If dfs function return False -> return False
        Mark node as visited
        Return True
        """
        visited[current] = 1

        for node in adjacency_list[current]:
            if visited[node] == 1:
                return False
            elif visited[node] == 0:
                if not self._canFinish(numCourses, adjacency_list, visited, node):
                    return False

        visited[current] = 2

        return True

    # id226 _Tree
    def invertTree(self, root: TreeNode) -> TreeNode:
        self._invertTree(root)
        return root

    def _invertTree(self, node: TreeNode):
        if node is None:
            return

        self._invertTree(node.left)
        self._invertTree(node.right)

        node.left, node.right = node.right, node.left

    # id235 _Tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Fill p_path and q_path with get_path
        Iterate for both path until first non-match
        Return last matched node
        """
        p_path, q_path = [], []

        def get_path(node: TreeNode, target: TreeNode, path: List[TreeNode]) -> None:
            """
            Append current node to path
            If target found -> return
            If node value greater than target -> dfs for left child
            Otherwise -> dfs for right child
            """
            path.append(node)

            if node.val == target.val:
                return

            if node.val > target.val:
                get_path(node.left, target, path)
            else:
                get_path(node.right, target, path)

        get_path(root, p, p_path)
        get_path(root, q, q_path)

        i = 0

        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            i += 1

        return p_path[i - 1]

    # id257 _Tree _DepthFirstSearch
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
        Go recursive from root with empty path list:
        If node is None -> []
        If node is leaf -> list wrapped string full path (create copy of path and append value)
        Otherwise -> append value to path and gather results from children
        Delete value from path
        Return merged results of two children
        """
        return self._binaryTreePaths(root, [])

    def _binaryTreePaths(self, node: TreeNode, path: List[int]) -> List[str]:
        if node is None:
            return []

        if node.left is None and node.right is None:
            dummy = path[:]
            dummy.append(node.val)
            return ['->'.join([str(num) for num in dummy])]

        path.append(node.val)

        left_result = self._binaryTreePaths(node.left, path)
        right_result = self._binaryTreePaths(node.right, path)

        path.pop()

        left_result.extend(right_result)

        return left_result

    # id230 _BinarySearch _Tree
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self._kthSmallest(root, k, [0])[1]

    def _kthSmallest(self, node: TreeNode, k: int, level: List[int]) -> int:
        if node is None:
            return 0

        left = self._kthSmallest(node.left, k, level)

        if level[0] == k:
            return left

        level[0] += 1

        if level[0] == k:
            return node.val

        right = self._kthSmallest(node.right, k, level)

        if level[0] == k:
            return right

        return level[0]

    # id450 _Tree
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        If root value must be deleted ->
            If right child is null -> return left one
            If left child is null -> return right one
            Otherwise ->
                Go one child right and maximum to the left (finding next larger value in tree)
                After node with value found
                Mark root value with found value
                And delete in right subtree founded (original value)
        If root value greater than key -> delete in left subtree
        Otherwise -> delete in right subtree
        """
        if not root:
            return None

        if root.val == key:
            if not root.right:
                return root.left

            if not root.left:
                return root.right

            if root.left and root.right:
                large = root.right

                while large.left:
                    large = large.left

                root.val = large.val
                root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root

    # id463 _HashTable
    # Todo: see ht
    # Todo: write solution
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return self._islandPerimeter(grid, [[False for _ in row] for row in grid], i, j)

    def _islandPerimeter(self, grid: List[List[int]], visited: List[List[bool]], i: int, j: int) -> int:
        visited[i][j] = True

        result = 4

        if -1 < i + 1 < len(grid) and -1 < j < len(grid[0]) and grid[i + 1][j] == 1:
            result -= 1

            if not visited[i + 1][j]:
                result += self._islandPerimeter(grid, visited, i + 1, j)

        if -1 < i - 1 < len(grid) and -1 < j < len(grid[0]) and grid[i - 1][j] == 1:
            result -= 1

            if not visited[i - 1][j]:
                result += self._islandPerimeter(grid, visited, i - 1, j)

        if -1 < i < len(grid) and -1 < j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
            result -= 1

            if not visited[i][j + 1]:
                result += self._islandPerimeter(grid, visited, i, j + 1)

        if -1 < i < len(grid) and -1 < j - 1 < len(grid[0]) and grid[i][j - 1] == 1:
            result -= 1

            if not visited[i][j - 1]:
                result += self._islandPerimeter(grid, visited, i, j - 1)

        return result

    # id501 _Tree
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

    # id543 _Tree
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        If root is null -> return 0
        Return decremented diameter of tree (diameter is number of edges in path)
        """
        if not root:
            return 0

        def height_and_diameter(node: TreeNode) -> (int, int):
            """
            If node is null -> return 0 (height) and -1 (diameter)
            Find left and right child results
            Return height (incremented maximum of both children) and
                diameter (maximum of diameter of two children and current node diameter)
            """
            if not node:
                return 0, -1

            left = height_and_diameter(node.left)
            right = height_and_diameter(node.right)

            return max(left[0], right[0]) + 1, max(left[1], right[1], left[0] + 1 + right[0])

        return height_and_diameter(root)[1] - 1

    # id547 _DepthFirstSearch _UnionFind
    def findCircleNum(self, M: List[List[int]]) -> int:
        """
        Init count for every outer call of dfs function
        Each dfs function:
        Visit friend as visited
        For every not visited friend (friend: index equal 1): call dfs function
        Thus, each outer call of dfs should visit one circle friends
        Return count of circles
        """
        count, visited = 0, [False for _ in M]

        for i in range(len(M)):
            if not visited[i]:
                count += 1
                self._findCircleNum(M, visited, i)

        return count

    def _findCircleNum(self, M: List[List[int]], visited: List[bool], index: int) -> None:
        visited[index] = True

        for i in range(len(M)):
            if M[index][i] == 1:
                if not visited[i]:
                    self._findCircleNum(M, visited, i)

    # id563 _Tree
    def findTilt(self, root: TreeNode) -> int:
        """
        Launch dfs from root
        Return second element (sum of tilts)
        """
        return self._findTilt(root)[1]

    def _findTilt(self, node: TreeNode) -> (int, int):
        """
        If node is child of leaf -> return 0 (sum of children values) and 0 (sum of tilts)
        Launch dfs from left and right children
        Return sum of values and sum of tilts (current and previous)
        """
        if node is None:
            return 0, 0

        left = self._findTilt(node.left)
        right = self._findTilt(node.right)

        return left[0] + right[0] + node.val, left[1] + right[1] + abs(left[0] - right[0])

    # id617 _Tree
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        Return merged two trees
        """
        def merge(first: TreeNode, second: TreeNode) -> TreeNode:
            """
            If both node not null -> update first node values with second node
            If only first not null -> stay first
            If only second not null -> init first with values of second
            Otherwise -> return null
            Return (updated) first
            """
            if first:
                if second:
                    first.val += second.left
                    first.left = merge(first.left, second.left)
                    first.right = merge(first.right, second.right)
            else:
                if second:
                    first = TreeNode(second.val)
                    first.left = merge(None, second.left)
                    first.right = merge(None, second.right)

            return first

        return merge(t1, t2)

    # id841 _DepthFirstSearch _Tree
    # Todo: see alternative for count
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Store opened door in opened as True
        If count of opened door equal to number of rooms -> return True (all rooms visited)
        Otherwise -> iterate over all keys in current room:
            If door not opened -> visit door with recursion
            If recursion returned True -> return True (all rooms visited)
            If left for loop -> return False (count not reached number of rooms)
        Note: count initialized as list for storing count value by pointer (in one branch of recursion we can open door
        which can be used in other branch)
        """
        return self._canVisitAllRooms(rooms, [0], [False for _ in rooms], 0)

    def _canVisitAllRooms(self, rooms: List[List[int]], count: List[int], opened: List[bool], current: int) -> bool:
        opened[current] = True
        count[0] += 1

        if count[0] == len(rooms):
            return True

        for key in rooms[current]:
            if not opened[key]:
                if self._canVisitAllRooms(rooms, count, opened, key):
                    return True

        return False

    # id988 _Tree _DepthFirstSearch
    def smallestFromLeaf(self, root: TreeNode) -> str:
        """
        If root is only node -> convert value to char
        Otherwise -> go recursive:
        If node is None -> 'large' string
        If node is leaf -> reversed and converted to chars string path
        Otherwise -> append value to path and gather paths from children
        Delete value from path
        Return smallest children results
        """
        if root.left is None and root.right is None:
            return chr(ord('a') + root.val)

        return self._smallestFromLeaf(root, [])

    def _smallestFromLeaf(self, node: TreeNode, path: List[int]) -> str:
        if node is None:
            return 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'

        if node.left is None and node.right is None:
            dummy = path[:]
            dummy.append(node.val)

            return ''.join([chr(ord('a') + num) for num in dummy[::-1]])

        path.append(node.val)

        left_result = self._smallestFromLeaf(node.left, path)
        right_result = self._smallestFromLeaf(node.right, path)

        path.pop()

        if left_result < right_result:
            return left_result
        else:
            return right_result
