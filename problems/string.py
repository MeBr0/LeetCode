

# noinspection PyMethodMayBeStatic
class Solution:
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

    def addStrings(self, num1: str, num2: str) -> str:
        """
        Start from the last element
        Calculate sum of digits and transferred digit
        Set digit to remainder to 10
        Set transfer to quotient to 10
        Repeat for each left digit
        If some digit absent in one of nums -> ignore its value
        If both digits absent -> append leading transfer if it is not zero
        """
        i = 1
        first_len = len(num1)
        second_len = len(num2)
        result = ''
        transfer = 0

        while True:
            if i <= first_len:
                if i <= second_len:
                    _sum = int(num1[-i]) + int(num2[-i]) + transfer
                    result = str(_sum % 10) + result
                    transfer = _sum // 10
                else:
                    _sum = int(num1[-i]) + transfer
                    result = str(_sum % 10) + result
                    transfer = _sum // 10

            else:
                if i <= second_len:
                    _sum = int(num2[-i]) + transfer
                    result = str(_sum % 10) + result
                    transfer = _sum // 10
                else:
                    if transfer != 0:
                        result = str(transfer) + result

                    break

            i += 1

        return result

    def reverseWords(self, s: str) -> str:
        """
        Strip s
        Split by spaces and reverse
        Join elements by space
        """
        return ' '.join(s.strip().split()[::-1])

