from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Save each number in dict[value, index]
        If matching for current number found in dict -> pair found
        """
        saved = {}

        for i, num in enumerate(nums):
            other = target - num

            if other in saved:
                return [i, saved[other]]

            saved[num] = i

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

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Start from the last element and increment it
        If number is 10 -> zero it and increment left digit (cycle)
        If left most digit incremented is 10 -> zero it and append 1 as first element
        """
        right = len(digits) - 1

        while True:
            if right < 0:
                digits.insert(0, 1)
                break
            else:
                digits[right] += 1

            if digits[right] != 10:
                break

            digits[right] = 0
            right -= 1

        return digits

    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        """
        Add each digit from K to A (If no digit -> insert)
        Start from the last element
        Set number to remainder to 10
        Set transfer to quotient to 10
        Repeat for each left digit
        """
        i = 1

        while K != 0:
            if i > len(A):
                A.insert(0, K % 10)
            else:
                A[-i] += K % 10
            K //= 10
            i += 1

        transfer = 0

        right = len(A) - 1

        while True:
            if right < 0:
                if transfer != 0:
                    A.insert(0, transfer)
                break
            else:
                A[right] += transfer

            transfer = A[right] // 10
            A[right] = A[right] % 10
            right -= 1

        return A

    # Todo: see bit manipulation
    def missingNumber(self, nums: List[int]) -> int:
        """
        Calculate overall sum of digits in range(len(nums))
        Take away each num in nums
        Return remainder
        """
        nums_len = len(nums)
        _sum = nums_len * (nums_len + 1) // 2

        for num in nums:
            _sum -= num

        return _sum
