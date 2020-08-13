from utils import ListNode


# noinspection PyMethodMayBeStatic
class Solution:
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
