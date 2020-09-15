from typing import List


# noinspection PyMethodMayBeStatic,PyRedeclaration
class Solution:
    # id53 _Array _DynamicProgramming _DivideAndConquer
    # Todo: see dp, d&c
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Set _max as first number and current as 0
        Iterate over nums:
        If current already negative -> null it
        Add num in current
        Compare _max with current
        If greater -> override _max
        Return _max
        """
        _max, current = nums[0], 0

        for num in nums:
            if current < 0:
                current = 0

            current += num
            _max = max(_max, current)

        return _max

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
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
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

    # id300 _BinarySearch _DynamicProgramming
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Let dp[i] is length of LIS ending in i
        Then dp[0] = 1
        For each next dp ->
            For each previous dp ->
                If current element greater than j-th -> save max length as maximum of previous value and dp[j]
            If max length found -> dp[i] = incremented max length
            Otherwise -> dp[i] = 1
        Return maximum dp values (max length)
        """
        if len(nums) == 0:
            return 0

        dp = [1]
        i = 1

        while i < len(nums):
            max_len = -1
            j = 0

            while j < i:
                if nums[i] > nums[j]:
                    max_len = max(max_len, dp[j])

                j += 1

            if max_len != -1:
                dp[i].append(max_len + 1)
            else:
                dp[i].append(1)

            i += 1

        return max(dp)

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
        nums_len = len(nums)

        if nums_len < 2:
            return nums_len

        dp = [-10 ** 9] + [10 ** 9 for _ in nums]
        i = 1

        while i <= len(nums):
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
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        Create list of lists sum_range and make it prefix sum from matrix
        Fill first row and column as usual prefix sums
        Next fill matrix with sum of two neighbours and difference of i - 1 j - 1 element
        """
        self.sum_range = []

        if len(matrix) != 0:
            self.sum_range = [
                [
                    0 for _ in range(len(matrix[i]))
                ] for i in range(len(matrix))
            ]

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
        _sum = self.sum_range[row2][col2]

        if col1 > 0:
            _sum -= self.sum_range[row2][col1 - 1]
        if row1 > 0:
            _sum -= self.sum_range[row1 - 1][col2]
        if row1 > 0 and col1 > 0:
            _sum += self.sum_range[row1 - 1][col1 - 1]

        return _sum
