# id295 _Heap _Design
# Todo: understand and write solution
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        from queue import PriorityQueue
        self.left = PriorityQueue()
        self.right = PriorityQueue()

    def addNum(self, num: int) -> None:
        self.left.put(-num)
        self.right.put(-self.left.get())

        if self.left.qsize() < self.right.qsize():
            self.left.put(-self.right.get())

    def findMedian(self) -> float:
        if self.left.qsize() != self.right.qsize():
            return self.left.queue[0]
        else:
            return (self.right.queue[0] + self.left.queue[0]) / 2
