

# noinspection PyMethodMayBeStatic
class Solution:
    # $20 $String $Stack
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
