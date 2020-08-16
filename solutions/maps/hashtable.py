from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    # $1 $Array $HashTable
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

    # $136 $HashTable $BitManipulation
    # Todo: see bm
    def singleNumber(self, nums: List[int]) -> int:
        """
        Xor first element with other elements
        Since a xor a = 0 and a xor 0 = a -> nums[0] is single number
        """
        for num in nums[1:]:
            nums[0] ^= num

        return nums[0]

    # $599 $HashTable
    # Todo: too slow
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        Count all restaurants appeared in both lists with their sum of indices
        Get minimum sum
        Iterate counter and return restaurant with minimum sum of indices
        """
        counter = {}
        indices = []

        for i, restaurant in enumerate(list1):
            if restaurant in list2:
                counter[restaurant] = i + list2.index(restaurant)

        min_index = min(counter.values())

        for restaurant, index_sum in counter:
            if index_sum == min_index:
                indices.append(restaurant)

        return indices

