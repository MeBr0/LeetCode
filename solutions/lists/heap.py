from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    # id215
    # Todo: see d&c
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Put nums to priority queue
        Retrieve (len - k) times element (till k-th largest)
        Return it
        """
        from queue import PriorityQueue
        queue = PriorityQueue()

        for num in nums:
            queue.put(num)

        i = 0
        value = None
        while i < len(nums) - k + 1:
            value = queue.get()

            i += 1

        return value

    # id264
    # Todo: see dp
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        from queue import PriorityQueue

        queue = PriorityQueue()
        queue.put(1)
        seen = {1: True}
        nums = (2, 3, 5)

        i = 1

        while i < n:
            x = queue.get()

            for num in nums:
                if x * num not in seen:
                    seen[x * num] = True
                    queue.put(x * num)

            i += 1

        return queue.get()

    # id378
    # Todo: see bs (heap too slow)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Insert all elements from matrix to priority queue
        Pop k times smallest element
        Return last one
        """
        from queue import PriorityQueue
        queue = PriorityQueue()

        for row in matrix:
            for num in row:
                queue.put(num)

        i = 0
        value = None

        while i < k:
            value = queue.get()

        return value
