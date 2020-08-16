

# noinspection PyMethodMayBeStatic,DuplicatedCode
class Solution:
    # 268 #Array #Math #BitManipulation
    # Todo: see bit manipulation solution
    def missingNumber(self, nums: List[int]) -> int:
        """
        Calculate overall sum of digits in range(len(nums))
        Take away each num in nums
        Return remainder
        """
        nums_len = len(nums)
        _sum = nums_len * (nums_len + 1) // 2

        for num in nums:
            _sum -= num

        return _sum

    # 7 #Math
    def reverse(self, x: int) -> int:
        """
        If negative invert -> save that it is negative
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

    # 9 #Math
    def isPalindrome(self, x: int) -> bool:
        """
        If x is negative -> it is not palindrome
        Reverse x
        If x equal to its inverse -> x is palindrome
        """
        if x < 0:
            return False

        return x == self.reverse(x)

    def _reverse(self, x: int) -> int:
        return self.reverse(x)

    # 171 #Math
    def titleToNumber(self, s: str) -> int:
        """
        Every letter is digit in 26-ary system
        Decode any letter to it value by ascii
        Add to result value times its power (i.e. 26 ** i)
        Return result
        """
        result, i, count = 0, 0, 26

        while i < len(s):
            char = s[-i - 1]

            result = (ord(char) - ord('A')) * count ** i
            i += 1

        return result

    # 168 #Math
    def convertToTitle(self, n: int) -> str:
        """
        While number is not 0:
        Decrement it (because A is 1)
        Calculate value by taking mod 26
        Append to result as left most converted char
        Return result
        """
        result, count = '', 26

        while n != 0:
            n -= 1

            value = n % count
            result = chr(value + ord('A') - 1) + result

            n //= 26

        return result

    # 1317 #Math
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """
        Iterate till (half) list:
        If 0 not appear in string representation of first and its inverse -> [first, n - first]
        """
        for first in range(1, n):
            if '0' not in ''.join([str(first), str(n - first)]):
                return [first, n - first]

    # 231 #Math #BitManipulation
    def isPowerOfTwo(self, n: int) -> bool:
        """
        If n == 0 -> False
        While n != 1:
        If n divisible by 2 -> divide by 2
        Otherwise -> False
        Return True
        """
        if n == 0:
            return False

        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                return False

        return True
