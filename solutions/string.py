

# noinspection PyMethodMayBeStatic,PyShadowingBuiltins
class Solution:
    # $8 $Math $String
    def myAtoi(self, str: str) -> int:
        """
        Iterate over str
        If space and already started to count result (info about digits, if it is negative or positive) -> break
        Otherwise -> continue
        If plus sign and not started to count result -> mark positive
        Otherwise -> break
        If minus sign and not started to count result -> mark negative
        Otherwise -> break
        If numeric -> mark numeric and append result to the right
        Otherwise -> break
        If negative marked -> invert result
        Lastly -> check for INT limit
        """
        result = 0
        negative, positive, numeric = False, False, False
        _max, _min = 2 ** 31 - 1, -2 ** 31

        for ch in str:
            if ch == ' ':
                if numeric or negative or positive:
                    break
                else:
                    continue
            elif ch == '+':
                if not negative and not positive and not numeric:
                    positive = True
                else:
                    break
            elif ch == '-':
                if not negative and not positive and not numeric:
                    negative = True
                else:
                    break
            elif ch.isnumeric():
                numeric = True
                result = result * 10 + int(ch)
            else:
                break

        if negative:
            result = -result

        if result > _max:
            return _max
        elif result < _min:
            return _min
        else:
            return result

    # $415 $String
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

    # $151 $String
    def reverseWords(self, s: str) -> str:
        """
        Strip s
        Split by spaces and reverse
        Join elements by space
        """
        return ' '.join(s.strip().split()[::-1])
