from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    # id20 _String _Stack
    def isValid(self, s: str) -> bool:
        """
        Create pair of parentheses in dict
        If it is opening item -> append to stack
        If it is closing item -> check last element for matching with dict
        If matching -> remove last element, else -> not valid
        """
        stack = []

        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for ch in s:
            if ch in parentheses:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                if parentheses.get(stack[-1]) != ch:
                    return False

                stack.pop()

        return len(stack) == 0

    # id150 _Stack
    # Todo: too slow
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Create stack for numbers
        If string is numeric (handle negatives) -> append to stack
        Otherwise -> pop last two numbers and perform current operation
        (In case of division -> truncate to zero)
        Return last (single) element in stack (i.e. result)
        """
        stack = []

        for token in tokens:
            copy = token[:]
            if copy.lstrip('-').isnumeric():
                stack.append(int(token))
            else:
                if token == '+':
                    second = stack.pop()
                    first = stack.pop()

                    stack.append(first + second)
                elif token == '-':
                    second = stack.pop()
                    first = stack.pop()

                    stack.append(first - second)
                elif token == '*':
                    second = stack.pop()
                    first = stack.pop()

                    stack.append(first * second)
                elif token == '/':
                    import math
                    second = stack.pop()
                    first = stack.pop()

                    stack.append(math.trunc(first / second))

        return int(stack.pop())

    # id848 _TwoPointers _Stack
    # Todo: see tp
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
        Append each character in string to stack:
        If # found -> pop last character (backspace it)
        Return whether both strings equal
        """
        return self._backspaceCompare(S) == self._backspaceCompare(T)

    def _backspaceCompare(self, string: str):
        stack = []

        for char in string:
            if char == '#':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
