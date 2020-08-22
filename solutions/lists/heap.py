from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    # id215 _DivideAndConquer _Heap
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
