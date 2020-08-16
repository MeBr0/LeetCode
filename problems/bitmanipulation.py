

# noinspection PyMethodMayBeStatic
class Solution:
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
