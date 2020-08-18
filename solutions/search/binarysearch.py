from typing import List


# noinspection PyMethodMayBeStatic,DuplicatedCode,PyRedeclaration
class Solution:
    # id33 _Array _BinarySearch
    def search(self, nums: List[int], target: int) -> int:
        """
        Use Binary Search with initial interval 0 and length
        If mid number equal target -> return mid index
        If mid number greater than left number ->
            If target not within interval [left number, mid number] -> search in right half
            Otherwise -> search in left half
        Otherwise ->
            If target within interval [mid number, right number] -> search in left half
            Otherwise -> search in right half
        If left from while -> target not found
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            _mid = (left + right) // 2

            if nums[_mid] == target:
                return _mid

            if nums[left] <= nums[_mid]:
                if target > nums[_mid] or target < nums[left]:
                    left = _mid + 1
                else:
                    right = _mid - 1
            else:
                if target < nums[_mid] or target > nums[right]:
                    right = _mid - 1
                else:
                    left = _mid + 1

        return -1

    # id69 _Math _BinarySearch
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

    # id153 _Array _BinarySearch
    def findMin(self, nums: List[int]) -> int:
        """
        Use Binary Search with initial interval 0 and length
        If middle number greater than last element -> minimum number in right part
        Otherwise -> minimum number in left part
        Return number with left index
        """
        left, right = 0, len(nums) - 1

        while left < right:
            _mid = (left + right) // 2

            if nums[_mid] > nums[right]:
                left = _mid + 1
            else:
                right = _mid

        return nums[left]

    # id278 _BinarySearch
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

    # id367 _Math _BinarySearch
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

    # id374 _BinarySearch
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
