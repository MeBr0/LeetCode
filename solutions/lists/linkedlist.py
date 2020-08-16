from utils import ListNode


# noinspection PyMethodMayBeStatic,PyTypeChecker,PyRedeclaration,DuplicatedCode,PyPep8Naming
class Solution:
    # id2 _LinkedList _Math
    # Todo: see math
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Iterate from the right digits
        Create dummy node root and copy pointer to it
        While there are some nodes or transfer digit:
        Calculate sum of node values and transfer digit
        Create linked node with remainder to 10
        Set transfer with quotient to 10
        Link each node to next one
        Return dummy node next
        """
        transfer = 0
        root = ListNode()
        node = root

        while l1 or l2 or transfer:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0

            _sum = first + second + transfer
            node.next = ListNode(_sum % 10)
            transfer = _sum // 10
            node = node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return root.next

    # id83 _LinkedList
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        If head is None -> None
        Create dummy _head pointer
        While there is not None node and next one is not None too:
        If value of current is equal to value of next -> link next of current to the next of next node
        Otherwise -> go to next node
        Return initial pointer to head
        """
        if head is None:
            return None

        _head = head

        while _head is not None and _head.next is not None:
            _next = _head.next

            if _head.val == _next.val:
                _head.next = _next.next
            else:
                _head = _head.next

        return head

    # id82 _LinkedList
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Create dummy node before head
        If two next nodes have same values -> Iterate next nodes until duplicate values gone, link next to new value
        Otherwise -> next node
        Return dummy node next (original head)
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next is not None and current.next.next is not None:
            if current.next.val == current.next.next.val:
                duplicate = current.next.val

                while current.next is not None and current.next.val == duplicate:
                    current.next = current.next.next

            else:
                current = current.next

        return dummy.next

    # id160 _LinkedList
    # Todo: re-read solution
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Create two pointers for lists
        While they not intersected:
        Link each node to the next one
        If reach the end of one list, link to head of another
        """
        intercept_a, intercept_b = headA, headB

        while intercept_a != intercept_b:
            intercept_a = intercept_a.next if intercept_a is not None else headB
            intercept_b = intercept_b.next if intercept_b is not None else headA

        return intercept_a
