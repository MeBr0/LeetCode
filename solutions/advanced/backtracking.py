from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
# Todo: simplify all recursion
class Solution:
    # id17 _String _Backtracking
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Init dict with numbers and letters
        Gather current index, all previous character
        Within _letterCombination:
        If previous has length of digits -> return list of generated string (empty for empty list)
        Otherwise ->
            For all characters in letters for current index:
            Append letter to previous
            Extend result with next character
            Pop letter
        Return result
        """
        numbers = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        return self._letterCombination(digits, 0, [], numbers)

    def _letterCombination(self, digits: str, index: int, previous: List[str], numbers: dict) -> List[str]:
        if len(previous) == len(digits):
            if len(previous) != 0:
                return [''.join(previous)]
            else:
                return []

        result = []

        for char in numbers[digits[index]]:
            previous.append(char)
            result.extend(self._letterCombination(digits, index + 1, previous, numbers))
            previous.pop()

        return result

    # id22 _String _Backtracking
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Gather in previous all parenthesis
        Within _generateParenthesis:
        Balance is difference between opened and closed parenthesis
        If length of previous reach maximum (2 * n) ->
            If balance is 0 -> return list with one valid string
            Otherwise -> return empty list
        Otherwise ->
            If balance is zero or balance less than remaining space (can be added open parenthesis) ->
                add it with incremented balance
            If balance greater than zero (can be added closed parenthesis) -> add it with decremented balance
        Return merged result of two operations
        """
        return self._generateParenthesis(n * 2, [], 0)

    def _generateParenthesis(self, _max: int, previous: List[str], balance: int) -> List[str]:
        if len(previous) == _max:
            if balance == 0:
                return [''.join(previous)]
            else:
                return []

        _open, close = [], []

        if balance == 0 or _max - len(previous) > balance:
            previous.append('(')
            _open = self._generateParenthesis(_max, previous, balance + 1)
            previous.pop()

        if balance > 0:
            previous.append(')')
            close = self._generateParenthesis(_max, previous, balance - 1)
            previous.pop()

        _open.extend(close)

        return _open

    # id37 _HashTable _Backtracking
    # Todo: write solution
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, columns, boxes = {i: [] for i in range(9)}, \
                               {i: [] for i in range(9)}, \
                               {i: [] for i in range(9)}

        for i in range(9):
            for j in range(9):
                el = board[i][j]

                if el == '.':
                    continue

                rows[i].append(el)
                columns[j].append(el)
                boxes[3 * (i // 3) + j // 3].append(el)

        self._solveSudoku(board, rows, columns, boxes, 0, 0)

    def _solveSudoku(self, board: List[List[str]], rows: dict, columns: dict, boxes: dict, i: int, j: int) -> bool:
        if i == 9:
            return True

        if board[i][j] != '.':
            return self._solveSudoku(board, rows, columns, boxes, i + (j + 1) // 9, (j + 1) % 9)

        for k in range(1, 10):
            char = str(k)

            if char not in rows[i] and char not in columns[j] and char not in boxes[3 * (i // 3) + j // 3]:
                rows[i].append(char)
                columns[j].append(char)
                boxes[3 * (i // 3) + j // 3].append(char)
                board[i][j] = str(char)

                if self._solveSudoku(board, rows, columns, boxes, i + (j + 1) // 9, (j + 1) % 9):
                    return True

                rows[i].remove(char)
                columns[j].remove(char)
                boxes[3 * (i // 3) + j // 3].remove(char)
                board[i][j] = '.'

        return False

    # id39 _Array _Backtracking
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Gather all numbers, last index and sum of numbers to consider:
        If _sum of previous is equal target -> return copy of previous
        Otherwise ->
            Iterate from last index (do not repeat combinations) to candidates:
            If sum of _sum and current number less or equal target ->
                Append element to previous
                Get result and extend result with it
                Pop element
        Return result
        """
        return self._combinationSum(candidates, [], 0, 0, target)

    def _combinationSum(self, candidates: List[int], previous: List[int], last_index: int, _sum: int, target: int) -> List[List[int]]:
        if _sum == target:
            return [previous[:]]

        result = []

        for i in range(last_index, len(candidates)):
            if _sum + candidates[i] <= target:
                previous.append(candidates[i])
                result.extend(self._combinationSum(candidates, previous, i, _sum + candidates[i], target))
                previous.pop()

        return result

    # id46 _Backtracking
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Gather in previous all previous numbers:
        Used is bit mask for used elements in nums
        Within _subsets:
        If count is equal to length of nums -> return cope of previous
        Otherwise -> Iterate over nums:
            If number not used (i-th bit is zero) -> extend result with new level recursion with i-th used
        Return result
        """
        return self._permute(nums, [], 0)

    def _permute(self, nums: List[int], previous: List[int], used: int) -> List[List[int]]:
        result = []

        if len(previous) == len(nums):
            return [previous[:]]

        for i in range(len(nums)):
            if not used & (1 << i):
                previous.append(nums[i])
                result.extend(self._permute(nums, previous, used | (1 << i)))
                previous.pop()

        return result

    # id78 _Array _Backtracking _BitManipulation
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Gather in previous all previous numbers
        Within _subsets:
        If count is equal to length of nums -> all numbers gathered, return (copy of) it
        Otherwise -> count _subsets with and without current element, merge results and return
        Return all subsets from recursion
        """
        return self._subsets(nums, [], 0)

    def _subsets(self, nums: List[int], previous: List[int], count: int) -> List[List[int]]:
        if count == len(nums):
            return [previous[:]]

        without = self._subsets(nums, previous, count + 1)

        previous.append(nums[count])
        _with = self._subsets(nums, previous, count + 1)
        previous.pop()

        _with.extend(without)

        return _with

    # id79 _Array _Backtracking
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Create 2-d matrix for used elements
        Iterate over matrix while first character of word not found:
        If found -> start _exist from element with char index 0:
            Mark element as used
            If char index is last element's -> return True (word found)
            Check all adjacent elements for boundaries, used and next character matching
            If all succeed -> go for next element
            Mark element as unused
            Return any result from 4 adjacent elements
        Return any result from matching of first character in matrix
        """
        used = [[False for _ in board[0]] for _ in board]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self._exist(board, used, i, j, word, 0):
                        return True

        return False

    def _exist(self, board: List[List[str]], used: List[List[bool]], i: int, j: int, word: str, char_i: int) -> bool:
        used[i][j] = True

        if char_i == len(word) - 1:
            return True

        result = False

        if self._exist_check(board, used, i + 1, j, word[char_i + 1]):
            result = result or self._exist(board, used, i + 1, j, word, char_i + 1)

        if self._exist_check(board, used, i - 1, j, word[char_i + 1]):
            result = result or self._exist(board, used, i - 1, j, word, char_i + 1)

        if self._exist_check(board, used, i, j + 1, word[char_i + 1]):
            result = result or self._exist(board, used, i, j + 1, word, char_i + 1)

        if self._exist_check(board, used, i, j - 1, word[char_i + 1]):
            result = result or self._exist(board, used, i, j - 1, word, char_i + 1)

        used[i][j] = False

        return result

    def _exist_check(self, board: List[List[str]], used: List[List[bool]], i: int, j: int, char: str):
        if i >= len(board) or i < 0:
            return False

        if j >= len(board[0]) or j < 0:
            return False

        if used[i][j]:
            return False

        return board[i][j] == char

    # id494 _DynamicProgramming _DepthFirstSearch
    # Todo: see dp
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        Init memoization for calculated sums for single element and sum (+ 1000 for positive indices)
        If index shifted to end of nums ->
            If calculated value matched with S -> return 1
            Otherwise -> return 0
        If value of sum calculated in memo -> return it
        Otherwise -> calculate for adding and subtracting value, save and return it
        """
        memo = [[-99999999999999999 for _ in range(2001)] for _ in nums]
        return self._findTargetSumWays(nums, 0, 0, S, memo)

    def _findTargetSumWays(self, nums: List[int], value: int, index: int, S: int, memo: List[List[int]]) -> int:
        if index == len(nums):
            if value == S:
                return 1
            else:
                return 0

        if memo[index][value + 1000] != -99999999999999999:
            return memo[index][value + 1000]

        plus = self._findTargetSumWays(nums, value + nums[index], index + 1, S, memo)
        minus = self._findTargetSumWays(nums, value - nums[index], index + 1, S, memo)

        memo[index][value + 1000] = plus + minus

        return memo[index][value + 1000]
