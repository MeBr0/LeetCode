

# noinspection PyMethodMayBeStatic
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int

        Use Binary Search with initial interval 1 and n
        If _mid is bad -> search in left part
        Otherwise -> search in right part
        """
        left, right = 1, n

        while left < right:
            _mid = (left + right) // 2

            if isBadVersion(_mid):
                right = _mid
            else:
                left = _mid + 1

        return left
