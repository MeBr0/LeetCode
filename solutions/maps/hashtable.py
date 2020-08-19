from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    # id1 _Array _HashTable
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

    # id599 _HashTable
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

    # id771 _HashTable
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        Create dictionary with values of J
        Iterate over S and check every character in jewels
        If in jewels -> increment count
        Return count
        """
        jewels, count = {}, 0

        for char in J:
            jewels[char] = True

        for char in S:
            if jewels.get(char):
                count += 1

        return count
