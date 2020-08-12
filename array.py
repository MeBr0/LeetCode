from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Save each number in dict[value, index]
        If matching for current number found in dict -> pair found
        """
        saved = {}

        for i, num in enumerate(nums):
            other = target - num

            if other in saved:
                return [i, saved[other]]

            saved[num] = i

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0

        for i, num in enumerate(nums1):
            if j > len(nums2):
                return

            if nums1[i] > nums2[j]:
                if nums1[i] != 0:
                    self._cycle_shift(nums1, i, len(nums1))

                nums1[i] = nums2[j]
                j += 1

            else:
                nums1[i] = nums2[j]
                j += 1

    def _cycle_shift(self, _list: List[int], start: int, end: int):
        for i in range(end - 1, start - 1, -1):
            if _list[i] == 0:
                continue

            _list[i], _list[i - 1] = _list[i - 1], _list[i]
