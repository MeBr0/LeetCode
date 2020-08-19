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
