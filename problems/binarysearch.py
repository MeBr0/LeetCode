

# noinspection PyMethodMayBeStatic
class Solution:
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

    def guessNumber(self, n: int) -> int:
        """
        Use Binary Search with initial interval 1 and n
        If _mid is less than n -> search in right part
        If _mid is greater than n -> search in left part
        Otherwise -> _mid (found)
        Return left most number (n == 1)

        Uses isBadVersion(int) function
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
