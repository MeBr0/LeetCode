

# noinspection PyMethodMayBeStatic
class Solution:
    # 278 #BinarySearch
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int

        Use Binary Search with initial interval 1 and n
        If _mid is bad -> search in left part
        Otherwise -> search in right part
        Return left most bound (first bad version)

        Uses isBadVersion(int) function
        """
        left, right = 1, n

        while left < right:
            _mid = (left + right) // 2

            if isBadVersion(_mid):
                right = _mid
            else:
                left = _mid + 1

        return left

    # 374 #BinarySearch
    def guessNumber(self, n: int) -> int:
        """
        Use Binary Search with initial interval 1 and n
        If _mid is less than n -> search in right part
        If _mid is greater than n -> search in left part
        Otherwise -> _mid (found)
        Return left most number (n == 1)

        Uses guess(int) function
        """
        left, right = 1, n

        while left < right:
            _mid = (left + right) // 2

            result = guess(_mid)

            if result < 0:
                right = _mid
            elif result > 0:
                left = _mid + 1
            else:
                return _mid

        return left

    # 69 #Math #BinarySearch
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

    # 367 #Math #BinarySearch
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
