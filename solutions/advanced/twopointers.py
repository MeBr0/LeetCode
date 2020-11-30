from typing import List

from utils import ListNode


# noinspection PyMethodMayBeStatic
class Solution:
    # id3 _HashTable _TwoPointers _String _SlidingWindow
    # Todo: see sw
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Init two pointers for sliding windows and hash table
        Iterate over characters in s:
        If char not saved or saved but expired (left greater) -> save new index
        Otherwise -> calculate maximum with difference of right and left, shift left for last appearance of character
        When left from while -> check _max again (for longest susbtring in the end of s)
        Return _max
        """
        saved = {}
        left, right, _max = 0, 0, -1

        while right < len(s):
            if s[right] not in saved or s[right] in saved and saved[s[right]] < left:
                saved[s[right]] = right
            else:
                _max = max(_max, right - left)
                left = saved[s[right]] + 1
                saved[s[right]] = right

            right += 1

        _max = max(_max, right - left)

        return _max

    # id11 _Array _TwoPointers
    def maxArea(self, height: List[int]) -> int:
        """
        Calculate area as minimum of height[left] and height[right] times
        difference of right and left
        Update area if this value is greater than current one
        Move pointer which has less value
        If they are equal -> move to greatest neighbour value
        Return area
        """
        left, right, area = 0, len(height) - 1, 0

        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                if height[left + 1] > height[right - 1]:
                    left += 1
                else:
                    right -= 1

        return area

    # id15 _Array _TwoPointers
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort nums
        Fix i-th element and solve twoSum with sorted array and value -nums[i]
        Append each matching to sums
        Return sums
        """
        sums = []
        nums.sort()

        for i in range(len(nums)):

            # Get rid of duplicates with continuing same fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    result = [nums[i], nums[left], nums[right]]
                    sums.append(result)

                    left += 1

                    # Get rid of duplicates with continuing same left element
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return sums

    # id16 _Array _TwoPointers
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Sort nums
        Fix i-th element and solve twoSum with sorted array and value -nums[i]
        If difference less than current -> update closest and difference
        Move one of pointers
        Return closest
        """
        closest, difference = None, 1 << 34
        nums.sort()

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while left < right:
                value = nums[left] + nums[right] + nums[i]

                if closest is None or difference > abs(target - value):
                    closest = value
                    difference = abs(target - value)

                if value > target:
                    right -= 1
                elif value < target:
                    left += 1
                else:
                    return closest

        return closest

    # id26 _Array _TwoPointers
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        """
        i, unique = 0, 0

        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                nums[unique], nums[i] = nums[i], nums[unique]
                unique += 1

            i += 1

        return unique

    # id27 _Array _TwoPointers
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        For every element in nums:
        If element equal to val -> Replace it by value of last element (dependent on right) and decrease right
        Otherwise -> next
        Return right
        """
        left, right = 0, len(nums)

        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1

        return right

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

    # id228 _Array
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Iterate over nums:
        Iterate till sequence not finished
        If start equal to finished (single number) -> append single number
        Otherwise -> append range of start and finish
        Iterate start to incremented finish
        Return result
        """
        start = 0
        result = []

        while start < len(nums):
            finish = start

            while finish + 1 < len(nums) and nums[finish] + 1 == nums[finish + 1]:
                finish += 1

            if start == finish:
                result.append(str(nums[finish]))
            else:
                result.append(str(nums[start]) + '->' + str(nums[finish]))

            start = finish + 1

        return result

    # id283 _Array _TwoPointers
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Iterate over nums and save last non_zero element set:
        If non zero element found -> swap with non_zero index
        """
        i, non_zero = 0, 0

        while i < len(nums):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1

            i += 1

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

    # id350 _HashTable _TwoPointers _BinarySearch _Sort
    # Todo: see ht, bs
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Sort lists
        Set two pointers to start of lists
        If elements equal -> append to result
        If first element greater -> increment second
        Otherwise -> increment first
        Return result
        """
        nums1.sort()
        nums2.sort()

        result = []
        first, second = 0, 0

        while first < len(nums1) or second < len(nums2):
            first_el = nums1[first]
            second_el = nums2[second]

            if first_el == second_el:
                result.append(first_el)
                first += 1
                second += 1
            elif first_el > second_el:
                second += 1
            else:
                first += 1

        return result

    # id680 _String
    def validPalindrome(self, s: str) -> bool:
        """
        While left less than right ->
            If characters not equal ->
                Return whether one valid palindrome of two substrings without left or right characters
            Move pointers nearer
        Return true (s already palindrome)
        """
        def check(i: int, j: int) -> bool:
            """
            Check whether substring of s between i and j is palindrome
            Compare pairs from begin and end
            """
            length = j + i

            while i < length / 2:
                if s[i] != s[length - 1 - i]:
                    return False

                i += 1

            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return check(left, right) or check(left + 1, right + 1)

            left += 1
            right -= 1

        return True
