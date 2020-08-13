

# noinspection PyMethodMayBeStatic
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        If needle is empty -> return 0
        If haystack is greater than needle -> return -1
        Iterate over haystack (till needle length from end)
        If first letter matched -> compare next letter till full needle covered
        If full needle found -> i, else -> -1
        """
        if needle == '':
            return 0

        haystack_len = len(haystack)
        needle_len = len(needle)

        if haystack_len < needle_len:
            return -1

        for i in range(haystack_len - needle_len + 1):
            if haystack[i] == needle[0]:
                full = True

                for j in range(1, needle_len):
                    if haystack[i + j] != needle[j]:
                        full = False
                        break

                if full:
                    return i

        return -1
