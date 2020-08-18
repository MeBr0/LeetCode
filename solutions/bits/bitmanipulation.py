from typing import List


# noinspection PyMethodMayBeStatic,PyRedeclaration
class Solution:
    # id191 _BitManipulation
    def hammingWeight(self, n: int) -> int:
        """
        While n != 0:
        If n & 1 == 1 (i.e. last bit is 1) -> count it
        Shift n to right by 1 one bit (i.e. remove last bit)
        Return counter
        """
        counter = 0

        while n != 0:
            if n & 1:
                counter += 1

            n = n >> 1

        return counter

    # id136 _HashTable _BitManipulation
    # Todo: see ht, math
    def singleNumber(self, nums: List[int]) -> int:
        """
        Xor first element with other elements
        Since a xor a = 0 and a xor 0 = a -> nums[0] is single number
        """
        for num in nums[1:]:
            nums[0] ^= num

        return nums[0]

    # id137 _BitManipulation
    # Todo: see ht, math
    # Todo: write solution
    def singleNumber(self, nums: List[int]) -> int:
        """
        Fuck it!
        """
        once, twice, not_thrice = 0, 0, 0

        for num in nums:
            twice |= (once & num)
            once ^= num

            not_thrice = ~(once & twice)
            once &= not_thrice
            twice &= not_thrice

        return once
