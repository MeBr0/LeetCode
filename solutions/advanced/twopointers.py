from typing import List

from utils import ListNode


# noinspection PyMethodMayBeStatic
class Solution:
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

    # id125 _TwoPointers _String
    def isPalindrome(self, s: str) -> bool:
        """
        While left less than right (i.e. two pointers from start and end):
        Pass any not alphanumeric char, till valid one for both pointers
        If characters lower representation are equal -> next iteration
        Otherwise -> not palindrome
        If left from outer while -> return True
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True

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

    # id167 _Array _TwoPointers _BinarySearch
    # Todo: see bs
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        While left less than right (i.e. two pointers from start and end):
        If sum of values equal target -> break
        If sum greater than target -> move right pointer
        Otherwise -> move left pointer
        Return last left-right pair
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            left_num = numbers[left]
            right_num = numbers[right]

            if left_num + right_num == target:
                break
            elif left_num + right_num > target:
                right -= 1
            else:
                left += 1

        return [left + 1, right + 1]

    # id344 _TwoPointers _String
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        While left less than right (i.e. two pointers from start and end):
        Swap both letters and shift pointers
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

    # id345 _TwoPointers _String
    def reverseVowels(self, s: str) -> str:
        """
        Convert s to list
        While left less than right (i.e. two pointers from start and end):
        Iterate each of two pointers while vowel not found
        Swap both vowels and shift pointers
        Return new string constructed from list
        """
        left, right = 0, len(s) - 1
        vowels = ['a', 'o', 'u', 'e', 'i']
        string = list(s)

        while left < right:
            while left < right and string[left].lower() not in vowels:
                left += 1
            while left < right and string[right].lower() not in vowels:
                right -= 1

            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

        return ''.join(string)

    # id680 _String
    def validPalindrome(self, s: str) -> bool:
        """
        While left less than right (i.e. two pointers from start and end):
        If characters equal -> next iteration
        Otherwise -> check for valid palindrome two substrings without left and right characters
        If left from while -> return True
        """
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self._validPalindrome(s[left: right]) or self._validPalindrome(s[left + 1: right + 1])

        return True

    def _validPalindrome(self, string: str) -> bool:
        i, size = 0, len(string)

        while i < size / 2:
            if string[i] != string[size - 1 - i]:
                return False

            i += 1

        return True
