

# noinspection PyMethodMayBeStatic,DuplicatedCode
class Solution:
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

    def mySqrt(self, x: int) -> int:
        """
        Use Binary search from 0 to half of x
        If square of mid is x or x between square or mid and square of next -> return mid
        If square of mid less than x -> shift left to the incremented mid
        If square of mid greater than x -> shift right to the decremented mid
        """
        if x == 1:
            return 1

        left, right = 0, x // 2

        while left <= right:
            mid = (left + right) // 2
            current = mid * mid
            _next = (mid + 1) * (mid + 1)

            if current == x or current < x < _next:
                return mid
            elif current < x:
                left = mid + 1
            else:
                right = mid - 1

        return 0

    def isPerfectSquare(self, num: int) -> bool:
        """
        Use Binary search from 0 to half of num
        If square of mid is num -> True
        If square of mid less than num -> shift left to the incremented mid
        If square of mid greater than num -> shift right to the decremented mid
        """
        if num == 1:
            return True

        left, right = 0, num // 2

        while left <= right:
            mid = (left + right) // 2
            current = mid * mid

            if current == num:
                return True
            elif current < num:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def myAtoi(self, str: str) -> int:
        """
        Iterate over str
        If space and already started to count result (info about digits, if it is negative or positive) -> break
        Otherwise -> continue
        If plus sign and not started to count result -> mark positive
        Otherwise -> break
        If minus sign and not started to count result -> mark negative
        Otherwise -> break
        If numeric -> mark numeric and append result to the right
        Otherwise -> break
        If negative marked -> invert result
        Lastly -> check for INT limit
        """
        result = 0
        negative, positive, numeric = False, False, False
        _max, _min = 2 ** 31 - 1, -2 ** 31

        for ch in str:
            if ch == ' ':
                if numeric or negative or positive:
                    break
                else:
                    continue
            elif ch == '+':
                if not negative and not positive and not numeric:
                    positive = True
                else:
                    break
            elif ch == '-':
                if not negative and not positive and not numeric:
                    negative = True
                else:
                    break
            elif ch.isnumeric():
                numeric = True
                result = result * 10 + int(ch)
            else:
                break

        if negative:
            result = -result

        if result > _max:
            return _max
        elif result < _min:
            return _min
        else:
            return result

