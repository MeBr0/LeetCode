from typing import List


# noinspection PyMethodMayBeStatic,PyRedeclaration,PyPep8Naming
class Solution:
    # id78 _Array _Backtracking _BitManipulation
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Since total number of solutions is 2^n, iterate for 2 ** nums length:
        Create subset
        Iterate over all elements in nums and use i as bit mask (1 include number, 0 not include number)
        i & 1 get last bit
        If last bit is 1 -> append j-th element
        Otherwise -> miss it
        Remove last bit
        After subset constructed, append to result
        Return result
        """
        result = []

        for i in range(2 ** len(nums)):
            subset = []

            for j in range(len(nums)):
                if i & 1:
                    subset.append(nums[j])

                i >>= 1

            result.append(subset)

        return result

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

    # id190 _BitManipulation
    def reverseBits(self, n: int) -> int:
        """
        Append last bit of n to bits
        Right shift to remove last bit
        Fill remaining space (up to 32) with zeros
        Reverse bits
        Construct result with bits
        Return result
        """
        bits = []

        while n != 0:
            bits.append(n & 1)
            n >>= 1

        while len(bits) < 32:
            bits.append(0)

        bits.reverse()

        result = 0

        for i in range(len(bits)):
            result += bits[i] * 2 ** i

        return result

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

    # id201 _BitManipulation
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        After all and operations, only leave is common left bits of m and n
        Therefore iterate from last (31-st) to first (0) bit:
        Get i-th bit of each number
        If they equal ->
            If equal 1 -> set i-th bit of result to 1
            Otherwise -> i-th bit of result already 0
        Otherwise -> break (common left bits ended, other bits will be 0)
        Return result
        """
        i, result = 31, 0

        while i > -1:
            m_bit = 1 if (m & (1 << i)) > 0 else 0
            n_bit = 1 if (n & (1 << i)) > 0 else 0

            if m_bit == n_bit:
                if m_bit == 1:
                    result |= (1 << i)
            else:
                break

            i -= 1

        return result

    # id338 _DynamicProgramming _BitManipulation
    # Todo: see dp (bm is slow)
    def countBits(self, num: int) -> List[int]:
        """
        For every number within [0, num]:
        If last bit is 1 (check by & 1) -> increment count
        Remove last bit (right shift)
        Append count to result
        Return result
        """
        result = []

        for i in range(num + 1):
            count = 0

            while i != 0:
                if i & 1:
                    count += 1

                i >>= 1

            result.append(count)

        return result

    # id461 _BitManipulation
    def hammingDistance(self, x: int, y: int) -> int:
        """
        For every 31 bit:
        Get i-th bit of x and y
        If not equal -> increment distance
        Return distance
        """
        distance, i = 0, 0

        while i < 31:
            if x & (1 << i) != y & (1 << i):
                distance += 1

            i += 1

        return distance
