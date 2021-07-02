from typing import List

from utils import ListNode


# noinspection PyTypeChecker,PyPep8Naming
class Solution:
    # id23
    # Todo: see heap
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Each time divide list by two and merge them
        If length of list 0 -> return None
        If length of list 1 -> return node itself
        Otherwise -> divide list and get result of merge
        Then merge them into single list (see id21)
        Return next of dummy node
        """
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        _mid = len(lists) // 2

        left = self.mergeKLists(lists[:_mid])
        right = self.mergeKLists(lists[_mid:])

        left_most = ListNode()
        dummy = left_most

        while left is not None or right is not None:
            if left is None:
                dummy.next = ListNode(right.val)
                right = right.next
            elif right is None:
                dummy.next = ListNode(left.val)
                left = left.next
            elif left.val > right.val:
                dummy.next = ListNode(right.val)
                right = right.next
            else:
                dummy.next = ListNode(left.val)
                left = left.next

            dummy = dummy.next

        return left_most.next
