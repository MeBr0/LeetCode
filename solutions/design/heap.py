

# id295 _Heap _Design
# Todo: understand and write solution
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.

        Init two priority queues for two halves (left - reversed)
        Then left will retrieve maximum and right - minimum (two medians)
        """
        from queue import PriorityQueue
        self.left = PriorityQueue()
        self.right = PriorityQueue()

    def addNum(self, num: int) -> None:
        """
        Put element in left (negated because left - reversed)
        Put maximum element from left to right
        If queues not equal length - balance with put minimum element from right to left
        """
        self.left.put(-num)
        self.right.put(-self.left.get())

        if self.left.qsize() < self.right.qsize():
            self.left.put(-self.right.get())

    def findMedian(self) -> float:
        """
        If queues not equal length -> return maximum element from left
        Otherwise -> return average of maximum from left and minimum from right
        """
        if self.left.qsize() != self.right.qsize():
            return -self.left.queue[0]
        else:
            return (self.right.queue[0] - self.left.queue[0]) / 2
