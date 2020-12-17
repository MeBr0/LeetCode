from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    # id17 _String _Backtracking
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Init dict with numbers and letters
        Gather current index, all previous character
        """
        numbers = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        stack = []
        length = len(digits)

        def get_combinations(index: int) -> List[str]:
            """
            If previous has length of digits ->
                If previous not empty -> return list of generated string
                Else -> return empty list
            For all characters in letters for current index:
            Append letter to previous
            Extend result with next character
            Pop letter
            Return result
            """
            if len(stack) == length:
                return [] if length == 0 else [''.join(stack)]

            result = []

            for char in numbers[digits[index]]:
                stack.append(char)
                result.extend(get_combinations(index + 1))
                stack.pop()

            return result

        return get_combinations(0)

    # id22 _String _Backtracking
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Gather in previous all parenthesis
        Return generated parenthesis from given n
        """
        stack = []

        def generate(balance: int) -> List[str]:
            """
            Balance is difference between opened and closed parenthesis
            If length of previous reach maximum (2 * n) ->
                If balance is 0 -> return list with one valid string
                Otherwise -> return empty list
            If balance is zero or balance less than remaining space (can be added open parenthesis) ->
                add it with incremented balance
            If balance greater than zero (can be added closed parenthesis) -> add it with decremented balance
            Return merged result of two operations
            """
            if len(stack) == 2 * n:
                if balance == 0:
                    return [''.join(stack)]
                else:
                    return []

            opened, closed = [], []

            if balance == 0 or 2 * n - len(stack) > balance:
                stack.append('(')
                opened = generate(balance + 1)
                stack.pop()

            if balance > 0:
                stack.append(')')
                closed = generate(balance - 1)
                stack.pop()

            opened.extend(closed)

            return opened

        return generate(0)

    # id37 _HashTable _Backtracking
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Init list for storing values of rows, columns and boxes
        Box index can be calculated as i, j -> 3 * (i // 3) + j // 3
        Iterate through board and register every cell in rows, columns and boxes
        Return return result of solving sudoku (from first cell [0, 0])
        """
        rows = [[] for _ in range(len(board))]
        columns = [[] for _ in range(len(board))]
        boxes = [[] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                cell = board[i][j]

                if cell == '.':
                    continue

                rows[i].append(cell)
                columns[j].append(cell)
                boxes[3 * (i // 3) + j // 3].append(cell)

        def solve(x: int, y: int) -> bool:
            """
            If board filled (x is not valid row) -> return true (board filled with valid values)
            If cell is not empty -> return result of solving next cell
            For every value from 1 to 9 ->
                If value not registered in row, column and box ->
                    Add value and register it
                    If result of solving next cell -> return true
                    Remove value and unregister it
            Return false (not valid solution)
            """
            if x == 9:
                return True

            if board[x][y] != '.':
                return solve(x + (y + 1) // 9, (y + 1) % 9)

            for k in range(len(board)):
                char = str(k + 1)
                box = boxes[3 * (x // 3) + y // 3]

                if char not in rows[x] and char not in columns[y] and char not in box:
                    rows[x].append(char)
                    columns[y].append(char)
                    box.append(char)
                    board[x][y] = str(char)

                    if solve(x + (y + 1) // 9, (y + 1) % 9):
                        return True

                    rows[x].remove(char)
                    columns[y].remove(char)
                    box.remove(char)
                    board[x][y] = '.'

            return False

        solve(0, 0)

    # id39 _Array _Backtracking
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Gather all numbers, last index and sum of numbers
        Return list of list of numbers gathered from 0 index and 0 sum
        """
        stack = []
        length = len(candidates)

        def get_numbers(last: int, _sum: int) -> List[List[int]]:
            """
            If sum of previous elements equal target -> return copy of previous
            Iterate from last index (do not repeat combinations) to candidates:
            If addition of sum and current number less or equal target ->
                Append element to previous
                Get result and extend result with it
                Remove element
            Return result
            """
            if _sum == target:
                return [stack[:]]

            result = []

            for i in range(last, length):
                if _sum + candidates[i] <= target:
                    stack.append(candidates[i])
                    result.extend(get_numbers(i, _sum + candidates[i]))
                    stack.pop()

            return result

        return get_numbers(0, 0)

    # id46 _Backtracking
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Return permutations from nums
        """
        stack = []
        length = len(nums)

        def get_permutations(used: int) -> List[List[int]]:
            """
            Used is bit mask for used elements in nums (number whose bitmask say i-th element is present or not)
            If count is equal to length of nums -> return copy of previous
            Iterate over nums:
            If number not used (i-th bit is zero) ->
                Set i-th bit to one
                Extend result with new level recursion with i-th used
            Return result
            """
            result = []

            if len(stack) == length:
                return [stack[:]]

            for i in range(length):
                if not used & (1 << i):
                    stack.append(nums[i])
                    result.extend(get_permutations(used | (1 << i)))
                    stack.pop()

            return result

        return get_permutations(0)

    # id78 _Array _Backtracking _BitManipulation
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Return all subsets from recursion
        """
        stack = []
        length = len(nums)

        def _subsets(count: int) -> List[List[int]]:
            """
            If count is equal to length of nums -> all numbers gathered, return copy of it
            Count subsets with and without current element, merge results and return it
            """
            if length == count:
                return [stack[:]]

            without = _subsets(count + 1)

            stack.append(nums[count])
            _with = _subsets(count + 1)
            stack.pop()

            _with.extend(without)

            return _with

        return _subsets(0)

    # id79 _Array _Backtracking
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Create 2-d matrix for used elements (false default)
        Iterate over matrix while first character of word not found ->
            If find_word from element with char index 0 return true -> return true (word found)
        Return false (word not found)
        """
        used = [[False for _ in board[0]] for _ in board]

        def find_word(x: int, y: int, index: int) -> bool:
            """
            Mark element as used
            If char index is last element's -> return True (whole word found)
            Check all adjacent elements for boundaries, used and next character matching
            If any of them succeed -> go for next element
            If any of search return true -> return true (word found)
            Mark element as unused (word not found)
            Return false (word not found)
            """
            used[x][y] = True

            if index == len(word) - 1:
                return True

            pairs = ((1, 0), (-1, 0), (0, 1), (0, -1))

            for pair in pairs:
                _x, _y = x + pair[0], y + pair[1]

                if check_adjacent(_x, _y, word[index + 1]) and find_word(_x, _y, index + 1):
                    return True

            used[x][y] = False

            return False

        def check_adjacent(x: int, y: int, char: str):
            return -1 < x < len(board) and -1 < y < len(board[0]) and not used[x][y] and board[x][y] == char

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and find_word(i, j, 0):
                    return True

        return False

    # id357 _Math _DynamicProgramming _Backtracking
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        Init list with used digits
        Return count
        """
        used = [False for _ in range(10)]
        n = 10 ** n

        def count_unique(previous: int) -> int:
            """
            Previous is filled number
            If previous greater or equal n -> return 0 (not counted)
            For every 10 digits ->
                Miss 0 for first digit
                If digit not used ->
                    Append and used it
                    Save result to count
                    Remove and unused it
            Increment count to count previous itself
            Return count
            """
            count = 0

            if previous >= n:
                return count

            for i in range(10):
                if previous == 0 == i:
                    continue

                if not used[i]:
                    used[i] = True
                    previous = previous * 10 + i

                    count += count_unique(previous)

                    used[i] = False
                    previous //= 10

            count += 1

            return count

        return count_unique(0)

    # id494 _DynamicProgramming _DepthFirstSearch
    # Todo: see dp
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        Init memoization for calculated sums for single element and sum (+ 1000 for positive indices)
        Return count of ways to sum nums
        """
        min_int = -99999999999999999
        memo = [[min_int for _ in range(2001)] for _ in nums]
        length = len(nums)

        def find_ways(count: int, index: int) -> int:
            """
            If index shifted to end of nums ->
                If calculated value matched with S -> return 1 (count it)
                Otherwise -> return 0
            If value of sum not calculated in memo ->
                Calculate values for adding and subtraction
                Save them
            Return it
            """
            if index == length:
                return 1 if count == S else 0

            count_i = count + 1000

            if memo[index][count_i] == min_int:
                plus = find_ways(count + nums[index], index + 1)
                minus = find_ways(count - nums[index], index + 1)

                memo[index][count_i] = plus + minus

            return memo[index][count_i]

        return find_ways(0, 0)
