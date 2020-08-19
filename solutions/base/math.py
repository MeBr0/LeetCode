from typing import List


# noinspection PyMethodMayBeStatic,DuplicatedCode
class Solution:
    # id7 _Math
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

    # id9 _Math
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

    # id13 _Math _String
    def romanToInt(self, s: str) -> int:
        """
        Create converter with roman and int values
        Iterate over s and compare current and next characters
        If current value less than next (pass through converter) -> take away value (i.e. we have sth like IV == 5 - 1)
        Otherwise -> add value to _sum
        Return _sum
        """
        converter = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        _sum = 0

        for i in range(len(s)):
            if i != len(s) - 1:
                current = converter[s[i]]
                _next = converter[s[i + 1]]

                if current < _next:
                    _sum -= current
                else:
                    _sum += current
            else:
                _sum += converter[s[i]]

        return _sum

    # id168 _Math
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

    # id171 _Math
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

    # id231 _Math _BitManipulation
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

    # id268 _Array _Math _BitManipulation
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

    # id412
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Iterate each number from 1 to n:
        If i divisible by 3 and 5 -> append FizzBuzz
        If i divisible only by 3 -> append Fizz
        If i divisible only by 5 -> append Buzz
        Otherwise -> append string representation of number
        """
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    result.append('FizzBuzz')
                else:
                    result.append('Fizz')
            else:
                if i % 5 == 0:
                    result.append('Buzz')
                else:
                    result.append(str(i))

        return result

    # id836 _Math
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        Check two corner x and y separately
        If first x of rec1 greater than second x of rec2 -> return False (i.e. rec1 is to the right of rec2)
        If first x of rec2 greater than second x of rec1 -> return False (i.e. rec2 is to the right of rec1)
        If first y of rec1 greater than second y of rec2 -> return False (i.e. rec1 is above of rec2)
        If first y of rec2 greater than second x of rec1 -> return False (i.e. rec2 is above of rec1)
        Otherwise -> return True (i.e. other cases they are overlap)
        """
        if rec1[0] >= rec2[2] or rec2[0] >= rec1[2]:
            return False

        if rec1[1] >= rec2[3] or rec2[1] >= rec1[3]:
            return False

        return True

    # id1281 _Math
    def subtractProductAndSum(self, n: int) -> int:
        """
        Create sum and product variable
        Get last digit by % 10
        Add it to sum
        Multiply it to product
        Divide n by 10 for next digit
        Return difference between product and sum
        """
        _sum, product = 0, 1

        while n != 0:
            digit = n % 10
            _sum += digit
            product *= digit

            n //= 10

        return product - _sum

    # id1317 _Math
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """
        Iterate till (half) list:
        If 0 not appear in string representation of first and its inverse -> [first, n - first]
        """
        for first in range(1, n):
            if '0' not in ''.join([str(first), str(n - first)]):
                return [first, n - first]
