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

    # id19 _LinkedList _TwoPointers
    # Todo: make faster
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Iterate linked list
        Count size and save all nodes in dict
        If n is first element -> return second node
        Otherwise -> get node whose place before node to delete
        Cut node to delete from linked list
        Return head
        """
        nodes = {}
        dummy = head
        count = 0

        while dummy is not None:
            nodes[count] = dummy
            dummy = dummy.next
            count += 1

        if count == n:
            return head.next

        before = nodes[count - n - 1]
        before.next = before.next.next

        return head

    # id21 _LinkedList
    # Todo: less memory
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        If one of lists None -> return other
        Otherwise -> create new node with lower value and next it
        Link next one with new list nodes
        Return first head
        """
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val > l2.val:
            node = ListNode(l2.val)
            l2 = l2.next
        else:
            node = ListNode(l1.val)
            l1 = l1.next

        node.next = self.mergeTwoLists(l1, l2)

        return node

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

    # id86 _LinkedList _TwoPointers
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Create two linked list for less and more values
        Create two pointers for current last and head
        Iterate nodes in head:
        If value greater than x -> append in head_more
        Otherwise -> append in less_more
        If one of lists is None -> return other one
        Otherwise -> return merged list
        """
        head_less, less, head_more, more = None, None, None, None

        while head is not None:
            value = head.val

            if head.val < x:
                if head_less is None:
                    head_less = ListNode(value)
                    less = head_less
                else:
                    less.next = ListNode(value)
                    less = less.next
            else:
                if head_more is None:
                    head_more = ListNode(value)
                    more = head_more
                else:
                    more.next = ListNode(value)
                    more = more.next

            head = head.next

        if head_less is None:
            return head_more
        else:
            if head_more is None:
                return head_less
            else:
                less.next = head_more
                return head_less

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

    # id206 _LinkedList
    def reverseList(self, head: ListNode) -> ListNode:
        """
        For every node in original linked list:
        If first node -> create node in _head
        Otherwise -> create dummy node and link with previous _head, then override _head
        Return _head
        """
        dummy, _head = None, None

        while head is not None:
            if _head is None:
                _head = ListNode(head.val)
            else:
                dummy = ListNode(head.val)
                dummy.next = _head
                _head = dummy

            head = head.next

        return _head

    # id237 _LinkedList
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        Change value of node to the next
        Change next node to one more next (i.e. node with given value deleted)
        """
        node.val = node.next.val
        node.next = node.next.next
