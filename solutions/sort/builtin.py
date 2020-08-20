from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    # id56 _Array _Sort
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort intervals by first element, than by second
        (which means that intersecting intervals located near each other)
        For every neighbour intervals:
        If they are intersecting ->
            Create new interval coordinates
            Delete both current intervals
            Insert new one
        Otherwise -> iterate next
        Return merged intervals
        """
        intervals.sort(key=lambda pair: (pair[0], pair[1]))
        i = 0

        while i < len(intervals) - 1:
            first = intervals[i]
            second = intervals[i + 1]

            if first[1] >= second[0] or (first[0] == second[0] or first[1] == second[1]) and first[0] <= second[1]:
                new_from = min(first[0], second[0])
                new_to = max(first[1], second[1])

                del intervals[i]
                del intervals[i]

                intervals.insert(i, [new_from, new_to])

            i += 1

        return intervals

    # id215 _DivideAndConquer _Heap
    # Todo: see d&c, heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Sort nums
        Return k-th element from end
        """
        return sorted(nums)[-k]

    # id217 _Array _HashTable
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Sort nums
        Iterate over nums:
        If two elements equal -> return True (i.e. if duplicates exists, they are next to each other)
        Otherwise -> return False
        """
        nums = sorted(nums)

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False

    # id242 _HashTable _Sort
    # Todo: see ht
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Sort each string by characters and compare them
        (i.e. anagrams will have same sorted representations)p
        """
        return ''.join(sorted(s)) == ''.join(sorted(t))

    # id628 _Array _Math
    # Todo: see math?
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Sort nums
        Maximum product can be obtained from either product of two minimum negative numbers and maximum positive
            or three maximum positive numbers
        Return maximum of following
        """
        nums = sorted(nums)

        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])
