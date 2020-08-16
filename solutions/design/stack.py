

# $225 $Stack $Design
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.

        Use list as queue (append, pop(0) methods allowed)
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.

        Append element to queue
        Re-append all popped elements except x
        """
        self.queue.append(x)

        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


# $155 $Stack $Design
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.

        Use simple list and field for storing min value
        """
        self.stack = []
        self._min = 10000000000000

    def push(self, x: int) -> None:
        """
        If x is less than _min -> override _min
        Push x to stack
        """
        if self._min > x:
            self._min = x

        self.stack.append(x)

    def pop(self) -> None:
        """
        Remove last element
        If last element is _min -> search for new _min in stack
        """
        last = self.stack.pop()

        if self._min == last:
            self._min = 10000000000000

            for num in self.stack:
                self._min = min(self._min, num)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min
