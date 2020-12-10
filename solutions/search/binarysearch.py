from typing import List


# noinspection PyMethodMayBeStatic,DuplicatedCode,PyRedeclaration,PyPep8Naming
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

    # id34 _Array _BinarySearch
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Search by binary search for first appearance in outer while
        If target first found ->
            Save it as first and last appearance
            Do binary search to left for first appearance
            Do binary search to right for last appearance
        Return first and last appearances
        """
        left, right = 0, len(nums) - 1
        first, last = -1, -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                last = mid
                first = mid

                left_mid = mid

                while left <= left_mid:
                    first_mid = (left + left_mid) // 2

                    if nums[first_mid] == target:
                        first = first_mid
                        left_mid = first_mid - 1
                    else:
                        left = first_mid + 1

                right_mid = mid

                while right_mid <= right:
                    last_mid = (right_mid + right) // 2

                    if nums[last_mid] == target:
                        last = last_mid
                        right_mid = last_mid + 1
                    else:
                        right = last_mid - 1

                break

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [first, last]

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

    # id74 _Array _BinarySearch
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Since matrix has following conditions, it is list in form of matrix
        Do binary search but to converting i, j coordinates to one number and vice-versa
        If number equal target -> return True
        Otherwise -> shift to left or right
        Return False
        """
        x = len(matrix)
        y = len(matrix[0]) if x > 0 else 0
        left, right = 0, x * y - 1

        while left <= right:
            mid = (left + right) // 2

            i, j = mid // y, mid % y

            if matrix[i][j] == target:
                return True

            if matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

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

    # id287 _Array _TwoPointers _BinarySearch
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Sort nums for binary search
        For middle number
        If one of the neighbours are equal with number -> return it
        If number greater or equal to its index (+1) -> no duplicates from left (consider right half)
        Otherwise -> no duplicates from right (consider left half)
        """
        left, right = 0, len(nums) - 1

        nums.sort()

        while left < right:
            mid = (left + right) // 2

            if nums[mid - 1] == nums[mid] or nums[mid] == nums[mid + 1]:
                return nums[mid]

            if nums[mid] >= mid + 1:
                left = mid + 1
            else:
                right = mid - 1

    # id367 _Math _BinarySearch
    # Todo: see math
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

    # id852 _BinarySearch
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        """
        Use Binary Search with initial interval 0 and len(A)
        If middle number greater than next and less than previous -> return middle index (found it!)
        If numbers are increasing -> peak in left part (shift right to middle)
        Otherwise -> peak in right part (shift left to middle)
        """
        left, right = 0, len(A) - 1

        while left <= right:
            _mid = (left + right) // 2

            if A[_mid - 1] < A[_mid] > A[_mid + 1]:
                return _mid

            if A[_mid - 1] > A[_mid] > A[_mid + 1]:
                right = _mid
            else:
                left = _mid

    # id1201 _Math _BinarySearch
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def count(x: int) -> int:
            return x // a + x // b + x // c - x // lcm(a, b) - x // lcm(b, c) - x // lcm(c, a) + x // lcm(a, lcm(b, c))

        def gcd(x: int, y: int) -> int:
            if y == 0:
                return x

            if x < y:
                return gcd(y, x)

            return gcd(x % y, y)

        def lcm(x: int, y: int) -> int:
            return x * y // gcd(x, y)

        left, right = min(a, b, c), 2 * 10 ** 8

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= n:
                right = mid
            else:
                left = mid + 1

        return left
