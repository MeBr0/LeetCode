from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Xor first element with other element
        Since A xor A = 0 and A xor 0 = A -> nums[0] is single number
        """
        for num in nums[1:]:
            nums[0] ^= num

        return nums[0]
