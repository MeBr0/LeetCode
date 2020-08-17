from typing import List

from utils import ListNode


# noinspection PyMethodMayBeStatic
class Solution:
    # id88 _Array _TwoPointers
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Iterate with two pointer for each list
        If first num is greater -> replace it by second, shifting all other values to the end
        If indexing over zeros -> replace zero by second
        Otherwise -> i++
        """
        i, j = 0, 0

        while i < m + n and j < n:
            if nums1[i] > nums2[j]:
                temp = nums1[i]
                nums1[i] = nums2[j]
                k = i + 1

                while k < n + m:
                    nums1[k], temp = temp, nums1[k]
                    k += 1

                i += 1
                j += 1

            elif i >= m + j:
                nums1[i] = nums2[j]
                i += 1
                j += 1

            else:
                i += 1

    # id141 _LinkedList _TwoPointers
    def hasCycle(self, head: ListNode) -> bool:
        """
        If size of list is 0 or 1 -> False
        Create two pointers slow (one step) and fast (two step)
        While slow not matched with fast:
        If fast is None (no cycle) and fast.next is None (2 nodes without cycle) -> False
        Otherwise -> step each pointers
        Return True (slow and fast matched)
        """
        if head is None or head.next is None:
            return False

        slow, fast = head, head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next

        return True

    # id28 _TwoPointers _String
    def strStr(self, haystack: str, needle: str) -> int:
        """
        If needle is empty -> return 0
        If haystack is greater than needle -> return -1
        Iterate over haystack (till needle length from end)
        If first letter matched -> compare next letter till full needle covered
        If full needle found -> i, else -> -1
        """
        if needle == '':
            return 0

        haystack_len = len(haystack)
        needle_len = len(needle)

        if haystack_len < needle_len:
            return -1

        for i in range(haystack_len - needle_len + 1):
            if haystack[i] == needle[0]:
                full = True

                for j in range(1, needle_len):
                    if haystack[i + j] != needle[j]:
                        full = False
                        break

                if full:
                    return i

        return -1
