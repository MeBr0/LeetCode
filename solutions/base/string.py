from typing import List


# noinspection PyMethodMayBeStatic,PyShadowingBuiltins,PyPep8Naming,PyUnusedLocal,SpellCheckingInspection,PyRedeclaration
class Solution:
    # id6 _String
    def convert(self, s: str, numRows: int) -> str:
        """
        Create list for chars in every row
        Calculate delta (between chars for every row)
        Iterate over characters:
        Calculate index of list with delta
        If in Zig (going down) -> append to list with index
        Otherwise (going up) -> append to list with delta - index
        Return constructed string from rows
        """
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        delta = 2 * numRows - 2

        for i, char in enumerate(s):
            index = i % delta

            if index < numRows:
                rows[index].append(char)
            else:
                rows[delta - index].append(char)

        return ''.join(''.join(row) for row in rows)

    # id8 _Math _String
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

    # id14 _String
    # Todo: could be slow
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Create i as index of selected character, current as current character for prefix
        For every string:
        If current is None -> override it with character
        Otherwise -> If current not equal to character -> return result
        If current is still None -> break
        If everything is ok -> append current character to result, null current and increment i
        Return result
        """
        i, result, current = 0, '', None

        while True:
            for string in strs:
                if i == len(string):
                    return result

                if current is None:
                    current = string[i]
                else:
                    if current != string[i]:
                        return result

            if current is None:
                break

            result += current
            current = None
            i += 1

        return result

    # id 58 _String
    def lengthOfLastWord(self, s: str) -> int:
        """
        If s contains only from whitespaces or empty -> return 0
        Otherwise -> return length last word in list split by whitespaces
        """
        if s.strip() == '':
            return 0

        return len(s.split()[-1])

    # id151 _String
    def reverseWords(self, s: str) -> str:
        """
        Strip s
        Split by spaces and reverse
        Join elements by space
        """
        return ' '.join(s.strip().split()[::-1])

    # id165 _String
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Split both versions by separator
        Iterate over level revision numbers together
        If one of numbers None -> replace by 0
        Compare versions parsed to int (get rid of leading zeros)
        If versions equal -> next iteration
        If left from while -> return 0 (versions equal)
        """
        versions1, versions2 = version1.split('.'), version2.split('.')
        v1_size, v2_size = len(versions1), len(versions2)
        i = 0

        while i < v1_size or i < v2_size:
            v1 = int(versions1[i]) if i < v1_size else 0
            v2 = int(versions2[i]) if i < v2_size else 0

            if v1 == v2:
                i += 1
            elif v1 > v2:
                return 1
            else:
                return -1

        return 0

    # id273 _Math _String
    # Todo: write solution
    def numberToWords(self, num: int) -> str:
        """
        """
        if num == 0:
            return 'Zero'

        digits = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        teens = [
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ]
        sectors = ['', 'Thousand', 'Million', 'Billion']

        result = []
        counter = 0

        while num != 0:
            part_result = []
            part = num % 1000

            first = part // 100
            second = part // 10 - 10 * first
            third = part - 100 * first - 10 * second

            if first != 0:
                part_result.append(digits[first])
                part_result.append('Hundred')

            if second != 0:
                if second == 1:
                    part_result.append(teens[third])
                else:
                    part_result.append(tens[second])

                    if third != 0:
                        part_result.append(digits[third])
            else:
                if third != 0:
                    part_result.append(digits[third])

            if part_result:
                postfix = sectors[counter]

                if postfix != '':
                    part_result.append(postfix)

                result.insert(0, ' '.join(part_result))

            counter += 1
            num //= 1000

        return ' '.join(result)

    # id383 _String
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        For every character in ransomNone:
        If character not in magazine -> return False
        If count of character in ransomNote greater than in magazine -> return False
        If left from for -> return True
        """
        for char in ransomNote:
            if char not in magazine:
                return False
            elif ransomNote.count(char) > magazine.count(char):
                return False

        return True

    # id388
    def lengthLongestPath(self, input: str) -> int:
        """
        Split input by endlines (tabulation before each item will tell about level)
        For every item:
        Count level and remove all tabultaions
        Append to stack current item (stack act like file system)
        If level changed (new directory or file in other one) -> exit directory
        If item is file (dot in name) -> override longest with length of path to file)
        Return longest
        """
        items = input.split('\n')
        stack = []
        longest = 0

        for item in items:
            level = item.count('\t')
            item = item.replace('\t', '')

            while len(stack) > level:
                stack.pop()

            stack.append(item)

            if '.' in item:
                longest = max(longest, len('/'.join(stack)))

        return longest

    # id415 _String
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

    # id482
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        """
        Iterate from end:
        If char is not - -> append to word from start
        If length of word equal K -> append to parts (uppered) from start and empty word
        If after for cycle word not empty -> append to parts (uppered) from start
        Return parts joined by -
        """
        parts, word = [], ''

        for i in range(len(S) - 1, -1, -1):
            if S[i] != '-':
                word = S[i] + word

                if len(word) == K:
                    parts.insert(0, word.upper())
                    word = ''

        if word != '':
            parts.insert(0, word.upper())

        return '-'.join(parts)

    # id557 _String
    def reverseWords(self, s: str) -> str:
        """
        Reverse words in splitted s with whitespace and join with whitespace again
        """
        return ' '.join(string[::-1] for string in s.split())

    # id647 _String _DynamicProgramming
    # Todo: thinking
    def countSubstrings(self, s: str) -> int:
        for i in range(len(s)):
            for j in range(i, len(s)):
                pass

    # id657 _String
    def judgeCircle(self, moves: str) -> bool:
        """
        Create deltas for x and y axis (initial origin coordinates)
        For every D - decrement y, for every U - increment y
        For every L - decrement x, for every R - increment x
        Return whether x and y still origin coordinates
        """
        x, y = 0, 0

        for move in moves:
            if move == 'D':
                y -= 1
            elif move == 'U':
                y += 1
            elif move == 'L':
                x -= 1
            else:
                x += 1

        return x == 0 and y == 0

    # id722 _String
    # noinspection PyUnboundLocalVariable
    def removeComments(self, source: List[str]) -> List[str]:
        """
        For every line in code:
        If not block comment -> create new result_line
        For every char in line:
        If two symbols /* (open block commecnt) and not block comment -> block and increment one more
        If two symbols */ (close block commecnt) and block comment -> unblock and increment one more
        If two symbols // (open line comment) -> break line appending
        If not block comment -> append char
        If line ended and not block comment -> append line to result
        Return result
        """
        result = []
        block = False

        for line in source:
            i = 0

            if not block:
                result_line = []

            while i < len(line):
                if line[i:i + 2] == '/*' and not block:
                    block = True
                    i += 1
                elif line[i:i + 2] == '*/' and block:
                    block = False
                    i += 1
                elif line[i:i + 2] == '//' and not block:
                    break
                elif not block:
                    result_line.append(line[i])

                i += 1

            if result_line and not block:
                result.append(''.join(result_line))

        return result

    # id824 _String
    def toGoatLatin(self, S: str) -> str:
        """
        Iterate over words in split S:
        If first char is vowel -> append word with rules for vowels
        Otherwise -> append word with rules for consonants
        Append word
        Return whitespace joined string from result
        """
        result = []
        vowels = 'aeiou'
        i = 0

        for word in S.split():
            if word[0].lower() in vowels:
                result_word = word + 'ma' + 'a' * (i + 1)
            else:
                result_word = word[1:] + word[0] + 'ma' + 'a' * (i + 1)

            result.append(result_word)
            i += 1

        return ' '.join(result)
