from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Xor first element with other elements
        Since a xor a = 0 and a xor 0 = a -> nums[0] is single number
        """
        for num in nums[1:]:
            nums[0] ^= num

        return nums[0]
