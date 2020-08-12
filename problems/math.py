

# noinspection PyMethodMayBeStatic,DuplicatedCode
class Solution:
    def reverse(self, x: int) -> int:
        """
        If negative invert, save that it is negative
        Get last digit of x and add it to result
        Check for INT limit
        """
        result = 0
        negative = False

        if x < 0:
            negative = True
            x = -x

        while x != 0:
            last = x % 10
            x //= 10
            result = result * 10 + last

        if result > 2**31 - 1 or result < -2**31:
            return 0

        return -result if negative else result

    def isPalindrome(self, x: int) -> bool:
        """
        If x ig negative, it is not palindrome
        Reverse x
        If x equal to its inverse -> x is palindrome
        """
        if x < 0:
            return False

        return x == self.reverse(x)

    def _reverse(self, x: int) -> int:
        return self.reverse(x)
