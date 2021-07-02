from collections import Counter
from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming,PyRedeclaration
class Solution:
    # id26
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Iterate nums:
        If current element is equal to next ->
            Iterate with j for all equal elements:
            If they are equal -> delete first one
        Increment i
        Return new length of nums
        """
        i = 0

        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                j = i
                while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    del nums[j]

            i += 1

        return len(nums)

    # id27
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Iterate nums:
        If element equal to val -> delete it
        Otherwise -> increment i (In case of delete, same i will point to next element)
        Return new length of nums
        """
        i = 0

        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1

        return len(nums)

    # id35
    # Todo: see binary search solution
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Iterate nums
        If num is greater or equal to target -> i
        Otherwise -> length of nums (i.e. target must be at the end of nums)
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)

    # id48
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Make transpose matrix
        Reverse each row
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

    # id54
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Handle empty matrices
        Init x0 y0 x1 y1 as bounds from top, left, botom and right
        Extend result list to the four directions step by step
        If bounds cross each other -> break
        Return order list
        """
        if not matrix or not matrix[0]:
            return []

        order = []
        x0, y0, x1, y1 = 0, 0, len(matrix) - 1, len(matrix[0]) - 1

        while True:
            order.extend(matrix[x0][j] for j in range(y0, y1 + 1))
            x0 += 1

            if x0 > x1:
                break

            order.extend(matrix[i][y1] for i in range(x0, x1 + 1))
            y1 -= 1

            if y0 > y1:
                break

            order.extend(matrix[x1][j] for j in range(y1, y0 - 1, -1))
            x1 -= 1

            if x0 > x1:
                break

            order.extend(matrix[i][y0] for i in range(x1, x0 - 1, -1))
            y0 += 1

            if y0 > y1:
                break

        return order

    # id66
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

    # id73
    # Todo: see O(1) memory
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Store any pair of row and column when 0 spotted
        For every such pair:
        Zero row and column
        """
        rows_columns, zero_row = [], [0 for _ in matrix[0]]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows_columns.append((i, j))

        for row, column in rows_columns:
            matrix[row] = zero_row

            for _row in matrix:
                _row[column] = 0

    # id80
    # Todo: see tp
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums) - 2:
            if nums[i] == nums[i + 1] == nums[i + 2]:
                j = i

                while j < len(nums) - 2 and nums[j] == nums[j + 1] == nums[j + 2]:
                    del nums[j]

            i += 1

        return len(nums)

    # id118
    def generate(self, numRows: int) -> List[List[int]]:
        """
        For each row:
        Create row with first number 1
        If it is first row -> append row to result and continue
        Otherwise -> iterate through previous row pairs and append sum of pair to current row
        Append last 1 to row
        Append row to result
        Return result with rows
        """
        result = []

        for i in range(numRows):
            row = [1]

            if i == 0:
                result.append(row)
                continue

            previous = result[i - 1]

            for j in range(len(previous) - 1):
                row.append(previous[j] + previous[j + 1])

            row.append(1)

            result.append(row)

        return result

    # id119
    def getRow(self, rowIndex: int) -> List[int]:
        """
        For every value within [0, rowIndex]:
        Append to result combination of rowIndex and i
        Return result
        """
        result = []
        i = 0

        # Todo: check how it works (copy pasted from stackoverflow)
        def combination(n, r):
            import operator as op
            from functools import reduce

            r = min(r, n - r)

            numerator = reduce(op.mul, range(n, n - r, -1), 1)
            denominator = reduce(op.mul, range(1, r + 1), 1)

            return numerator // denominator

        while i != rowIndex + 1:
            result.append(combination(rowIndex, i))
            i += 1

        return result

    # id121
    # Todo: see dp solution
    def maxProfit(self, prices: List[int]) -> int:
        """
        Iterate over the list:
        If price is less than min_price -> override min_price
        If difference between price and min_price is greater profit than max_profit -> override max_profit
        Return max_profit
        """
        min_price, max_profit = 100000000000, 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

    # id122
    # Todo: determine whether this greedy
    def maxProfit(self, prices: List[int]) -> int:
        """
        Iterate over the list
        If price is less than min_price -> override min_price
        If difference between price and min_price is greater profit than max_profit ->
            check next nums till they decreasing
        After finding longest increasing sequence, add max_profit to _sum
        Set i to j - 1 (previous number while searching end of increasing sequence)
        """
        _sum, min_price, max_profit = 0, 100000000000, 0
        i = 0
        size = len(prices)

        while i != size:
            if prices[i] < min_price:
                min_price = prices[i]

            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

                j = i + 1

                while j != size and prices[j] > prices[j - 1]:
                    max_profit = prices[j] - min_price
                    j += 1

                _sum += max_profit
                min_price, max_profit = 100000000000, 0
                i = j - 1

            i += 1

        return _sum

    # id169
    # Todo: see d&c and bm solutions
    def majorityElement(self, nums: List[int]) -> int:
        """
        Count all elements
        Iterate counter:
        If count greater than half of length of nums -> num
        """
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, count in counter.items():
            if count > len(nums) // 2:
                return num

    # id229
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Count all elements
        Iterate counter:
        If count greater than thirds of length of nums -> append num to result
        Return result
        """
        counter, result = {}, []

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, count in counter.items():
            if count > len(nums) // 3:
                result.append(num)

        return result

    # id414
    def thirdMax(self, nums: List[int]) -> int:
        """
        Create three variables for first, second and third maximums
        Iterate over all numbers:
        If first not set or current number greater than first -> make second maximum third, first second, number first
        If current number equal to first -> ignore it
        If second not set or current number greater than second -> make first second, number first
        If current number equal to second -> ignore it
        If third not set or current number greater than third -> make number third
        If third not set -> return first maximum
        Otherwise -> return third maximum
        """
        first, second, third = None, None, None

        for num in nums:
            if first is None or num > first:
                third, second, first = second, first, num
            elif num == first:
                continue
            elif second is None or num > second:
                third, second = second, num
            elif num == second:
                continue
            elif third is None or num > third:
                third = num

        return first if third is None else third

    # id454
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        Merge four array into two arrays as pairwise sums
        Count elements in these arrays
        For each value in first:
            Search negative value in second:
                Append overall matching
        Return result
        """
        first = Counter([a + b for a in A for b in B])
        second = Counter([c + d for c in C for d in D])
        result = 0

        for num in first:
            if -num in second:
                result += first[num] * second[-num]

        return result

    # id509
    # Todo: see matrix exponential and golden ratio solutions
    def fib(self, N: int) -> int:
        """
        If N <= 1 -> N
        If N == 2 -> 1
        Create variables for two previous values, current value and index 3
        Iterate till N + 1:
        Override current value by sum of two previous
        Update previous values
        Return current
        """
        if N <= 1:
            return N

        if N == 2:
            return 1

        first, second, current, i = 1, 1, 0, 3

        while i < N + 1:
            current, first, second = first + second, second, current

            i += 1

        return current

    # id523
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = [0]

        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        length = len(prefix_sum)

        for i in range(length):
            for j in range(i + 1, length):
                if prefix_sum[j] - prefix_sum[i] % k == 0:
                    return True

        return False

    # id643
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix_sum = [0]

        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        return max([prefix_sum[i + k] - prefix_sum[i] for i in range(len(prefix_sum) - k)])

    # id674
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        If nums is empty -> return 0
        Create longest sequence size and current sequence size
        For every number compare with next number:
        If next one is greater -> increment current
        Otherwise -> sequence ended, override longest if current is greater and set current to 1
        After left from for override longest again (for last element)
        Return longest
        """
        length = len(nums)

        if length == 0:
            return 0

        longest, current = 1, 1

        for i in range(length - 1):
            if nums[i] < nums[i + 1]:
                current += 1
            else:
                longest = max(current, longest)
                current = 1

        return max(current, longest)

    # id766
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Iterate from left bottom corner to right top by edges:
        Iterate by diagonal:
        If num not set -> set num by first number
        Otherwise -> if number no match with num -> return False
        Shift i, j by edge to the top and afterwards, to the right
        If left from outer while -> return True
        """
        rows, columns = len(matrix), len(matrix[0])
        i, j = rows - 1, 0

        while j != columns:
            x, y, num = i, j, None

            while x != rows and y != columns:
                if num is None:
                    num = matrix[x][y]
                else:
                    if num != matrix[x][y]:
                        return False

                x, y = x + 1, y + 1

            if i != 0:
                i -= 1
            else:
                j += 1

        return True

    # id989
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

        transfer, right = 0, len(A) - 1

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

    # id1051
    # Todo: find better solution
    def heightChecker(self, heights: List[int]) -> int:
        """
        Create copy of heights and sort it
        Iterate over two lists
        If there is no matching -> increment count
        Return count
        """
        right_order = sorted(heights[:])
        count = 0

        for i in range(len(right_order)):
            if right_order[i] != heights[i]:
                count += 1

        return count

    # id1470
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Iterate over the half of list:
        Append num itself and num shifted from i by n
        Return result
        """
        result = []

        for i in range(len(nums) // 2):
            result.append(nums[i])
            result.append(nums[i + n])

        return result

    # id1893
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        _range = [False for _ in range(50)]

        for r in ranges:
            for i in range(r[0], r[1] + 1):
                _range[i - 1] = True

        for i in range(left, right + 1):
            if not _range[i - 1]:
                return False

        return True
