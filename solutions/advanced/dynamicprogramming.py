from typing import List


# noinspection PyMethodMayBeStatic,PyRedeclaration,PyPep8Naming
class Solution:
    # id5 _String _DynamicProgramming
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in s] for _ in s]

        for i in range(len(s)):
            dp[i][i] = True

        left, right = 0, 0

        for i in range(1, len(s)):
            for j in range(len(s) - i):
                right = j + i

                if right - j == 1:
                    if s[j] == s[right]:
                        dp[j][right] = True

                        if right - left < right - j:
                            right = right
                            left = j

                else:
                    if dp[j + 1][right - 1]:
                        if s[j] == s[right]:
                            dp[j][right] = True

                            if right - left < right - j:
                                right = right
                                left = j

        return s[left:right + 1]

    # id53 _Array _DynamicProgramming _DivideAndConquer
    # Todo: see dp, d&c
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Set _max as first number and current as 0
        Iterate over nums:
        If current already negative -> null it
        Add num in current
        Compare result with current
        If greater -> override result
        Return _max
        """
        result, current = nums[0], 0

        for num in nums:
            if current < 0:
                current = 0

            current += num
            result = max(result, current)

        return result

    # id62 _Array _DynamicProgramming
    def uniquePaths(self, m: int, n: int) -> int:
        """
        For upper and left borders set result 1
        For other cells result is sum of upper and left cells
        Return last cell in matrix
        """
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

    # id64 _Array _DynamicProgramming
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        For borders init prefix sums
        For other results add minimum of upper and left results
        Return last element
        """
        x, y = len(grid), len(grid[0])

        for i in range(1, x):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, y):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, x):
            for j in range(1, y):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]

    # id70 _DynamicProgramming
    def climbStairs(self, n: int) -> int:
        """
        Count result for first two stairs
        Each next result is sum of two previous results
        Return last (n-th) result
        """
        dp = [None, 1, 2]

        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n]

    # id91 _String _DynamicProgramming
    def numDecodings(self, s: str) -> int:
        """
        Check for special cases
        Create dp[0] as dummy value
        Let dp[i] is number of decodings finished at i-th index
        Then dp[1] = 1
        For each next dp ->
            If current char is valid decoding ->
                dp[i] includes all decodings from dp[i-1]

                If last two chars is valid decoding ->
                    dp[i] includes all decoding from dp[i-2]
            Else ->
                If last two chars is valid decoding ->
                    dp[i] includes all decoding from dp[i-2]
                Else ->
                    dp[i] = 0 (not valid decoding)
        Return dp[len(s)] as result
        """
        if s[0] == '0':
            return 0

        if len(s) < 2:
            return 1

        def valid(code: str) -> bool:
            """
            Check whether string is valid decoding
            """
            code_len = len(code)

            if code_len == 1:
                return code[0] != '0'
            elif code_len == 2:
                if code[0] == '0':
                    return False
                elif code[0] == '1':
                    return True
                elif code[0] == '2':
                    return code[1] <= '6'
                else:
                    return False
            else:
                return False

        dp = [1 for _ in range(len(s) + 1)]

        for i in range(2, len(s) + 1):
            if valid(s[i - 1]):
                dp[i] = dp[i - 1]

                if valid(s[i - 2:i]):
                    dp[i] += dp[i - 2]
            else:
                dp[i] = dp[i - 2]

                if not valid(s[i - 2:i]):
                    dp[i] = 0

        return dp[len(s)]

    # id139 _DynamicProgramming
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Let dp[i] whether can be broken prefix from 0 to i
        Then dp[0] is True (empty string)
        For each dp ->
            For each word ->
                If word is postfix in i-th and before postfix word is breakable ->
                    dp[i] = True
        Return dp[-1] as result for whole string
        """
        dp = [True] + [False for _ in s]

        def is_substr(target: str, end: int) -> bool:
            """
            Check whether target and s from
            (begin to end, same size as target) is equal
            """
            if end - len(target) - 1 < -1:
                return False

            delta = end - len(target)
            j = 0

            while j < len(target):
                if s[j + delta] != target[j]:
                    return False

                j += 1

            return True

        for i in range(len(s)):
            for word in wordDict:
                if is_substr(word, i + 1) and dp[i - len(word) + 1]:
                    dp[i + 1] = True

        return dp[-1]

    # id198 _DynamicProgramming
    def rob(self, nums: List[int]) -> int:
        """
        Check for special cases
        Let dp[i] - maximum amount of money from robbing from 0 to i-th houses
        Then dp[0] = nums[0], dp[1] = nums[1], dp[2] = nums[0] + nums[2]
        For each next dp ->
            dp[i] is nums[i] with maximum amount frm rubbing
            either i-2 or i-3 houses
        Return maximum of last two elements
        """
        length = len(nums)

        if length == 0:
            return 0

        if length <= 2:
            return max(nums)

        if length == 3:
            return max(nums[1], nums[0] + nums[2])

        dp = [0 for _ in nums]

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = dp[0] + nums[2]

        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])

        return max(dp[-1], dp[-2])

    # id300 _BinarySearch _DynamicProgramming
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Let dp[i] is last left element of LIS of length i
        Then dp[0] = MIN_INT
        For each next dp ->
            With binary search (since dp is ascending)
            Find rightest dp from previous which greater than current value
            Save current dp as minimum of current dp and current value
        Return first initialized dp from end
        """
        length = len(nums)

        if length < 2:
            return length

        dp = [-10 ** 9] + [10 ** 9 for _ in nums]
        i = 1

        while i <= length:
            left, right = 0, i

            while left < right:
                mid = (left + right) // 2

                if nums[i - 1] > dp[mid]:
                    dp[mid + 1] = min(dp[mid + 1], nums[i - 1])
                    left = mid + 1
                else:
                    right = mid

            i += 1

        i = len(dp) - 1

        while i > -1:
            if dp[i] != 10 ** 9:
                return i

            i -= 1

    # id322 _DynamicProgramming
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Let dp[i] is least number of coins with sum of i
        Then dp[0] = 0
        For each coin ->
            For each next dp from coin itself ->
                If i - coin can be charged with less coins than dp[i] (+1) -> override dp[i]
        If dp[amount] not initialized -> return -1
        Otherwise -> return it
        """
        dp = [0] + [10 ** 9 for _ in range(amount)]

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[-1] == 10 ** 9 else dp[-1]

    # id329 _DepthFirstSearch _TopologicalSort _Memoization
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Let dp[i][j] is longest increasing path ending in (i, j)
        Not counted dp[i][j] = -1 (marked as not used or calculated)
        For each row ->
            For each number ->
                Calculate dp[i][j] as incremented maximum of neighbour's dp
        Return maximum in dp
        """
        if len(matrix) == 0:
            return 0

        rows, columns = len(matrix), len(matrix[0])

        dp = [[-1 for _ in row] for row in matrix]
        pairs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def calculate(x: int, y: int):
            """
            If dp[x][y] already calculated -> return it
            For each neighbour ->
                If bounds valid and neighbour is less than current value ->
                    Save maximum of such values in adjacent
            Save in dp and return it
            """
            if dp[x][y] != -1:
                return dp[x][y]

            adjacent = 0

            for _x, _y in pairs:
                dx, dy = x + _x, y + _y

                if -1 < dx < rows and -1 < dy < columns and matrix[x][y] > matrix[dx][dy]:
                    adjacent = max(adjacent, calculate(dx, dy))

            dp[x][y] = adjacent + 1

            return dp[x][y]

        return max([calculate(i, j) for i in range(rows) for j in range(columns)])

    # id416 _DynamicProgramming
    # Todo: see faster solutions
    # Todo: write solution
    def canPartition(self, nums: List[int]) -> bool:
        """
        """
        _sum = sum(nums)

        if _sum % 2 == 1:
            return False

        half = _sum // 2

        dp = [[False for _ in range(half + 1)] for _ in nums]
        dp[0][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(half + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]

    # id486 _DynamicProgramming _Minimax
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
        Let dp[l][r] - score difference between players between l-th and r-th
        Return dp[0][-1]
        """
        dp = [[0 for _ in nums] for _ in nums]

        def winner(left: int, right: int) -> int:
            """
            If left == right ->
                Return nums[left] itself
            If dp[left][right] calculated ->
                Return it
            Calculate left and right result
            from dp[left+1][right] and dp[left][right-1]
            Update dp[left][right] as maximum of them
            Return dp[left][right]
            """
            if left == right:
                return nums[left]

            if dp[left][right]:
                return dp[left][right]

            left_result = nums[left] - winner(left + 1, right)
            right_result = nums[right] - winner(left, right - 1)

            dp[left][right] = max(left_result, right_result)

            return dp[left][right]

        return winner(0, len(nums) - 1) >= 0

    # id518
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Let dp[i] is number of combinations of coin with sum of i
        Then dp[0] = 1
        For each coin ->
            For each next dp from coin itself ->
                Add to i length combination i - coin combination because coin can be added
        Return dp[amount]
        """
        dp = [1] + [0 for _ in range(amount)]

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]

    # id746 _Array _DynamicProgramming
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Count result for first two stairs
        Each next result is minimum of two previous plus current cost
        Return minimum of two last elements
        """
        dp = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            dp.append(cost[i] + min(dp[i - 1], dp[i - 2]))

        return min(dp[-1], dp[-2])


# id303 _DynamicProgramming
# noinspection PyPep8Naming
class NumArray:
    def __init__(self, nums: List[int]):
        """
        Create list sum_range and make it prefix sum from nums
        """
        self.sum_range = []

        if len(nums) != 0:
            self.sum_range.append(nums[0])

            for i in range(1, len(nums)):
                self.sum_range.append(self.sum_range[-1] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        """
        If i is first element -> return j element
        Otherwise -> return difference between elements with indices j and i - 1
        """
        if i == 0:
            return self.sum_range[j]

        return self.sum_range[j] - self.sum_range[i - 1]


# id304 _DynamicProgramming
# noinspection PyPep8Naming
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        Create list of lists sum_range and make it prefix sum from matrix
        Fill first row and column as usual prefix sums
        Next fill matrix with sum of two neighbours and difference of i - 1 j - 1 element
        """
        self.sum_range = []
        x = len(matrix)

        if x != 0:
            y = len(matrix[0])

            self.sum_range = [[0 for _ in range(y)] for _ in range(x)]
            self.sum_range[0][0] = matrix[0][0]

            for i in range(1, len(self.sum_range[0])):
                self.sum_range[0][i] = self.sum_range[0][i - 1] + matrix[0][i]

            for i in range(1, len(self.sum_range)):
                self.sum_range[i][0] = self.sum_range[i - 1][0] + matrix[i][0]

            for i in range(1, len(self.sum_range)):
                for j in range(1, len(self.sum_range[i])):
                    self.sum_range[i][j] = self.sum_range[i - 1][j] + self.sum_range[i][j - 1] \
                                           + matrix[i][j] - self.sum_range[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Get right-bottom corner sum
        If col1 is not first column -> take away sum before it
        If row1 is not first row -> take away sum before it
        If both row1 and col1 are not first -> add sum before it (because for both col1 and row1, took away twice)
        Return _sum
        """
        result = self.sum_range[row2][col2]

        if col1 > 0:
            result -= self.sum_range[row2][col1 - 1]
        if row1 > 0:
            result -= self.sum_range[row1 - 1][col2]
        if row1 > 0 and col1 > 0:
            result += self.sum_range[row1 - 1][col1 - 1]

        return result
