from typing import List


# noinspection PyMethodMayBeStatic
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
