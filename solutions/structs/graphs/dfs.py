from typing import List

from utils import TreeNode, Node, ListNode, NAryNode


# noinspection PyShadowingBuiltins,PyPep8Naming,PyMethodMayBeStatic,PyTypeChecker,PyRedeclaration
class Solution:
    # id94
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node: TreeNode) -> List[int]:
            if node is None:
                return []

            order = []

            order.extend(dfs(node.left))
            order.append(node.val)
            order.extend(dfs(node.right))

            return order

        return dfs(root)

    # id98
    def isValidBST(self, root: TreeNode) -> bool:
        """
        For root set interval as huge negative and positive numbers
        For every node:
        If node is None -> True
        If node value within given interval (_min, _max) -> recursion for left and right nodes with new intervals
        Otherwise -> False
        """
        def dfs(node: TreeNode, _min: int, _max: int) -> bool:
            if node is None:
                return True

            if _min < node.val < _max:
                return dfs(node.left, _min, node.val) and dfs(node.right, node.val, _max)

            return False

        return dfs(root, -10000000000, 10000000000)

    # id100
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

    # id101
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

        def dfs(left: TreeNode, right: TreeNode) -> bool:
            if left is None or right is None:
                return left == right

            if left.val != right.val:
                return False

            return dfs(left.right, right.left) and dfs(left.left, right.right)

        return dfs(root.left, root.right)

    # id104
    def maxDepth(self, root: TreeNode) -> int:
        """
        If node is None -> 0
        Otherwise -> incremented maximum of children depth
        """
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # id105
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

    # id108
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

    # id109
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        Return root create from ListNode
        """
        dummy, size = head, 0

        while dummy is not None:
            dummy = dummy.next
            size += 1

        def node_from_sorted(left: int, right: int) -> TreeNode:
            if left >= right:
                return None

            mid = (left + right) // 2

            nonlocal head

            left = None if left == mid else node_from_sorted(left, mid)

            node = TreeNode(head.val)
            head = head.next
            node.left = left

            node.right = None if right == mid else node_from_sorted(mid + 1, right)

            return node

        return node_from_sorted(0, size)

    # id110
    def isBalanced(self, root: TreeNode) -> bool:
        """
        If node is None -> 0
        Compare depth of children subtrees
        If difference more than 1 or both or them have unbalanced children subtrees -> int_max
        Otherwise -> maximum depth
        :int_max is value of depth for unbalanced subtree
        """
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1 or left == 10000000000 and right == 10000000000:
                return 10000000000

            return max(left, right) + 1

        return dfs(root) != 10000000000

    # id112
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        Go recursive from root with current value 0:
        If node is None -> False
        If current (saved sum) + node.val == sum and node is leaf -> True
        Otherwise check children with updated current value (add node.val)
        """
        def dfs(node: TreeNode, current: int) -> bool:
            if node is None:
                return False

            new_value = current + node.val

            if new_value == sum and node.left is None and node.right is None:
                return True

            return dfs(node.left, new_value) or dfs(node.right, new_value)

        return dfs(root, 0)

    # id113
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
        path = []

        def dfs(node: TreeNode, current: int) -> List[List[int]]:
            if node is None:
                return []

            new_value = current + node.val

            if new_value == sum and node.left is None and node.right is None:
                result = path[:]
                result.append(node.val)
                return [result]

            path.append(node.val)

            left_result = dfs(node.left, new_value)
            right_result = dfs(node.right, new_value)

            path.pop()

            left_result.extend(right_result)

            return left_result

        return dfs(root, 0)

    # id116
    def connect(self, root: 'Node') -> 'Node':
        """
        Index of root is 1
        Return mutated root
        """
        nodes = {}

        def dfs(node: 'Node', index: int) -> 'Node':
            """
            If node is child of leaf -> return
            Start from right nodes (index 2 * x + 1, like heap)
            If current index not right most node (check by index is not 2 ** n - 1) -> link next with next node in nodes
            Register node in nodes with index
            End with left nodes (index 2 * x, like heap)
            """
            if node is None:
                return None

            dfs(node.right, index * 2 + 1)

            if not check(index):
                node.next = nodes[index + 1]

            nodes[index] = node

            dfs(node.left, index * 2)

            return node

        def check(index: int) -> bool:
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

        return dfs(root, 1)

    # id124
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
        num = -999999999999999

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            left_result = max(dfs(node.left), 0)
            right_result = max(dfs(node.right), 0)

            nonlocal num

            if left_result + right_result + node.val > num:
                num = left_result + right_result + node.val

            return node.val + max(left_result, right_result)

        dfs(root)

        return num

    # id129
    def sumNumbers(self, root: TreeNode) -> int:
        """
        Go recursive from root with empty path list:
        If node is None -> 0
        If node is leaf -> number constructed from digits in path
        Otherwise -> append value to path and gather results from children
        Delete value from path
        Return sum of results of two children
        """
        path = []

        def dfs(node: TreeNode) -> int:
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

            left_result = dfs(node.left)
            right_result = dfs(node.right)

            path.pop()

            return left_result + right_result

        return dfs(root)

    # id130
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

        def dfs(x: int, y: int, mode: bool) -> None:
            visited[x][y] = True

            if mode:
                board[x][y] = 'X'

            pairs = ((0, 1), (0, -1), (1, 0), (-1, 0))

            for pair in pairs:
                _x, _y = x + pair[0], y + pair[1]

                if check_range(_x, _y):
                    dfs(_x, _y, mode)

        def check_range(x: int, y: int) -> bool:
            return -1 < x < len(board) and -1 < y < len(board[0]) and check_value(x, y)

        def check_value(x: int, y: int) -> bool:
            return not visited[x][y] and board[x][y] == 'O'

        for i in range(len(board)):
            if check_value(i, 0):
                dfs(i, 0, False)
            if check_value(i, len(board[0]) - 1):
                dfs(i, len(board[0]) - 1, False)

        for j in range(len(board[0])):
            if check_value(0, j):
                dfs(0, j, False)
            if check_value(len(board) - 1, j):
                dfs(len(board) - 1, j, False)

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if check_value(i, j):
                    dfs(i, j, True)

    # id133
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodes = {}

        # noinspection PyShadowingNames
        def dfs(node: 'Node') -> 'Node':
            if not node:
                return None

            if node.val not in nodes:
                nodes[node.val] = Node(node.val)

            for pair in node.neighbors:
                if pair.val not in nodes:
                    nodes[pair.val] = dfs(pair)

                nodes[node.val].neighbors.append(nodes[pair.val])

            return nodes[node.val]

        return dfs(node)

    # id144
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node: TreeNode) -> List[int]:
            if node is None:
                return []

            order = [node.val]
            order.extend(dfs(node.left))
            order.extend(dfs(node.right))

            return order

        return dfs(root)

    # id145
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node: TreeNode) -> List[int]:
            if node is None:
                return []

            order = []

            order.extend(dfs(node.left))
            order.extend(dfs(node.right))
            order.append(node.val)

            return order

        return dfs(root)

    # id200
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

        def dfs(x: int, y: int) -> None:
            used[x][y] = True

            pairs = ((1, 0), (-1, 0), (0, 1), (0, -1))

            for pair in pairs:
                _x, _y = x + pair[0], y + pair[1]

                if check(_x, _y):
                    dfs(_x, _y)

        def check(x: int, y: int) -> bool:
            return -1 < x < len(grid) and -1 < y < len(grid[0]) and not used[x][y] and grid[x][y] == '1'

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not used[i][j] and grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count

    # id207
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

        def dfs(current: int) -> bool:
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
                    if not dfs(node):
                        return False

            visited[current] = 2

            return True

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False

        return True

    # id226
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode) -> TreeNode:
            if node is None:
                return

            dfs(node.left)
            dfs(node.right)

            node.left, node.right = node.right, node.left

            return node

        return dfs(root)

    # id235
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

    # id257
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
        Go recursive from root with empty path list:
        If node is None -> []
        If node is leaf -> list wrapped string full path (create copy of path and append value)
        Otherwise -> append value to path and gather results from children
        Delete value from path
        Return merged results of two children
        """
        path = []

        def dfs(node: TreeNode) -> List[str]:
            if node is None:
                return []

            if node.left is None and node.right is None:
                dummy = path[:]
                dummy.append(node.val)
                return ['->'.join([str(num) for num in dummy])]

            path.append(node.val)

            left_result = dfs(node.left)
            right_result = dfs(node.right)

            path.pop()

            left_result.extend(right_result)

            return left_result

        return dfs(root)

    # id230
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        level = 0

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            left = dfs(node.left)

            nonlocal level

            if level == k:
                return left

            level += 1

            if level == k:
                return node.val

            right = dfs(node.right)

            if level == k:
                return right

            return level

        return dfs(root)

    # id394
    def decodeString(self, s: str) -> str:
        strings = []
        num, string = '', ''
        found = 0

        for char in s:
            if char == '[':
                if found > 0:
                    string += char

                found += 1

            elif char == ']':
                found -= 1

                if found == 0:
                    strings.append(int(num) * self.decodeString(string))
                    num, string = '', ''
                else:
                    string += char

            else:
                if found > 0:
                    string += char
                else:
                    if char.isnumeric():
                        if string != '':
                            strings.append(string)

                        num += char
                    else:
                        strings.append(char)

        return s if len(strings) == 0 else ''.join(strings)

    # id450
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

    # id463
    # Todo: see ht
    # Todo: write solution
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in row] for row in grid]

        def dfs(x: int, y: int) -> int:
            visited[x][y] = True

            result = 4

            pairs = ((1, 0), (-1, 0), (0, 1), (0, -1))

            for pair in pairs:
                _x, _y = x + pair[0], y + pair[1]

                if -1 < _x < len(grid) and -1 < _y < len(grid[0]) and grid[_x][_y] == 1:
                    result -= 1

                    if not visited[_x][_y]:
                        result += dfs(_x, _y)

            return result

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)

    # id491
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        It is more backtracking
        """
        result = set()
        current = []

        def dfs(j: int) -> None:
            current.append(nums[j])

            if len(current) > 1:
                result.add(tuple(current))

            for k in range(j, len(nums)):
                if k == j:
                    continue

                if nums[k] >= nums[j]:
                    dfs(k)

            current.pop()

        for i in range(len(nums)):
            dfs(i)

        return result

    # id501
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
        result, count = [], {}

        if root is None:
            return result

        def dfs(node: TreeNode) -> None:
            if node is not None:
                count[node.val] = count.get(node.val, 0) + 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        mode = max(count.values())

        for value, frequency in count.items():
            if frequency == mode:
                result.append(value)

        return result

    # id529
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click

        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            pairs = ((1, 1), (1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1))

            def dfs(i: int, j: int) -> None:
                count = mine_count(i, j)

                if count == 0:
                    board[i][j] = 'B'

                    for di, dj in pairs:
                        _x, _y = i + di, j + dj

                        if -1 < _x < len(board) and -1 < _y < len(board[0]) and board[_x][_y] == 'E':
                            dfs(_x, _y)
                else:
                    board[i][j] = str(count)

            def mine_count(i: int, j: int) -> int:
                count = 0

                for di, dj in pairs:
                    _x, _y = i + di, j + dj

                    if -1 < _x < len(board) and -1 < _y < len(board[0]) and board[_x][_y] == 'M':
                        count += 1

                return count

            dfs(x, y)

        return board

    # id543
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        If root is null -> return 0
        Return decremented diameter of tree (diameter is number of edges in path)
        """
        if not root:
            return 0

        def dfs(node: TreeNode) -> (int, int):
            """
            If node is null -> return 0 (height) and -1 (diameter)
            Find left and right child results
            Return height (incremented maximum of both children) and
                diameter (maximum of diameter of two children and current node diameter)
            """
            if not node:
                return 0, -1

            left = dfs(node.left)
            right = dfs(node.right)

            return max(left[0], right[0]) + 1, max(left[1], right[1], left[0] + 1 + right[0])

        return dfs(root)[1] - 1

    # id547
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

        def dfs(index: int) -> None:
            visited[index] = True

            for k in range(len(M)):
                if M[index][k] == 1:
                    if not visited[k]:
                        dfs(k)

        for i in range(len(M)):
            if not visited[i]:
                count += 1
                dfs(i)

        return count

    # id559
    def maxDepth(self, root: 'NAryNode') -> int:
        def dfs(node: 'NAryNode', level: int) -> int:
            maxi = level

            if node is not None and node.children is not None:
                for child in node.children:
                    maxi = max(maxi, dfs(child, level + 1))

            return maxi

        return dfs(root, 1)

    # id563
    def findTilt(self, root: TreeNode) -> int:
        """
        Launch dfs from root
        Return second element (sum of tilts)
        """
        def dfs(node: TreeNode) -> (int, int):
            """
            If node is child of leaf -> return 0 (sum of children values) and 0 (sum of tilts)
            Launch dfs from left and right children
            Return sum of values and sum of tilts (current and previous)
            """
            if node is None:
                return 0, 0

            left = dfs(node.left)
            right = dfs(node.right)

            return left[0] + right[0] + node.val, left[1] + right[1] + abs(left[0] - right[0])

        return dfs(root)[1]

    # id617
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        Return merged two trees
        """
        def dfs(first: TreeNode, second: TreeNode) -> TreeNode:
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
                    first.left = dfs(first.left, second.left)
                    first.right = dfs(first.right, second.right)
            else:
                if second:
                    first = TreeNode(second.val)
                    first.left = dfs(None, second.left)
                    first.right = dfs(None, second.right)

            return first

        return dfs(t1, t2)

    # id700
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(node: TreeNode) -> TreeNode:
            if not node:
                return None

            if node.val == val:
                return node

            if val > node.val:
                return dfs(node.right)
            else:
                return dfs(node.left)

        return dfs(root)

    # id841
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
        count = 0
        opened = [False for _ in rooms]

        def dfs(index: int) -> bool:
            opened[index] = True

            nonlocal count
            count += 1

            if count == len(rooms):
                return True

            for key in rooms[index]:
                if not opened[key]:
                    if dfs(key):
                        return True

            return False

        return dfs(0)

    # id886
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        """
        Fuck N
        """
        from collections import defaultdict
        graph = defaultdict(list)

        for first, second in dislikes:
            graph[first].append(second)
            graph[second].append(first)

        colors = {}

        def dfs(node: int, color: int = 0) -> bool:
            if node in colors:
                return colors[node] == color

            colors[node] = color

            return all(dfs(adjacent, 1 - color) for adjacent in graph[node])

        return all(dfs(node) for node in graph if node not in colors)

    # id988
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

        path = []

        def dfs(node: TreeNode) -> str:
            if node is None:
                return 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'

            if node.left is None and node.right is None:
                dummy = path[:]
                dummy.append(node.val)

                return ''.join([chr(ord('a') + num) for num in dummy[::-1]])

            path.append(node.val)

            left_result = dfs(node.left)
            right_result = dfs(node.right)

            path.pop()

            if left_result < right_result:
                return left_result
            else:
                return right_result

        return dfs(root)

    # id1254
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in row] for row in grid]
        pairs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(x: int, y: int) -> bool:
            visited[x][y] = True
            closed = True

            for dx, dy in pairs:
                _x, _y = x + dx, y + dy

                if -1 < _x < len(grid) and -1 < _y < len(grid[0]):
                    if not visited[_x][_y] and grid[_x][_y] == 0:
                        if not dfs(_x, _y):
                            closed = False
                else:
                    closed = False

            return closed

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 0 and not dfs(i, j):
                    count += 1

        return count

    # id1306
    def canReach(self, arr: List[int], start: int) -> bool:
        used = [False for _ in arr]

        def dfs(index: int) -> bool:
            used[index] = True

            if arr[index] == 0:
                return True

            result = False

            if index + arr[index] < len(arr) and not used[index + arr[index]]:
                result = result or dfs(index + arr[index])

            if index - arr[index] > -1 and not used[index - arr[index]]:
                result = result or dfs(index - arr[index])

            return result

        return dfs(start)
