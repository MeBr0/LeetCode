from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming,PyRedeclaration
class Solution:
    # $66 $Array
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

    # $989 $Array
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

    # $35 $Array $BinarySearch
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

    # $118 $Array
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

    # $119 $Array
    def getRow(self, rowIndex: int) -> List[int]:
        """
        For every value within [0, rowIndex]:
        Append to result combination of rowIndex and i
        Return result
        """
        result = []
        i = 0

        while i != rowIndex + 1:
            result.append(self._combination(rowIndex, i))
            i += 1

        return result

    # Todo: check how it works (copy pasted from stackoverflow)
    def _combination(self, n, r):
        import operator as op
        from functools import reduce

        r = min(r, n - r)

        numerator = reduce(op.mul, range(n, n - r, -1), 1)
        denominator = reduce(op.mul, range(1, r + 1), 1)

        return numerator // denominator

    # $1470 $Array
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

    # $1051 $Array
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

    # $509 $Array
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
            current = first + second
            first = second
            second = current

            i += 1

        return current

    # $121 $Array $DynamicProgramming
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

    # $122 $Array $Greedy
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

    # $169 $Array $DivideAndConquer $BitManipulation
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

    # $229 $Array
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
