from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming,SpellCheckingInspection,PyShadowingBuiltins,PyRedeclaration
class Solution:
    # id1 _Array _HashTable
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Save each number in dict[value, index]
        If matching for current number found in dict -> pair found
        """
        saved = {}

        for i, num in enumerate(nums):
            other = target - num

            if other in saved:
                return [i, saved[other]]

            saved[num] = i

    # id36 _HashTable
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Create counted numbers for each row, column and sub-box
        Iterate over 2d list:
        If element is . -> continue
        If element already presented in row -> return False
        Otherwise -> add to current row
        If element already presented in column -> return False
        Otherwise -> add to current column
        If element already presented in box -> return False
        Otherwise -> add to current box
        Return True
        """
        rows, columns, boxes = {i: [] for i in range(9)}, \
                               {i: [] for i in range(9)}, \
                               {i: [] for i in range(9)}

        for i in range(9):
            for j in range(9):
                el = board[i][j]

                if el == '.':
                    continue

                if el in rows[i]:
                    return False
                else:
                    rows[i].append(el)

                if el in columns[j]:
                    return False
                else:
                    columns[j].append(el)

                box_index = 3 * (i // 3) + j // 3

                if el in boxes[box_index]:
                    return False
                else:
                    boxes[box_index].append(el)

        return True

    # id49 _HashTable _String
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Init hash table with sorted chars and list of strings
        Iterate over strs:
        If sorted chars of string already in anagrams -> register string
        Otherwise -> append string
        Return values of anagrams
        """
        anagrams = {}

        for string in strs:
            chars = ''.join(sorted(string))

            if chars not in anagrams:
                anagrams[chars] = [string]
            else:
                anagrams[chars].append(string)

        return list(anagrams.values())

    # id217 _Array _HashTable
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Init hash table
        If number already in hash table -> return True (number previously be registered in table)
        Otherwise -> register number in table
        Return False
        """
        once = {}

        for num in nums:
            if num in once:
                return True
            else:
                once[num] = True

        return False

    # id219 _Array _HashTable
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Create hash table for last appearance of number
        If number already appeared ->
            If difference between indeces not exceeded k -> return True
            Otherwise -> update last appearance
        Otherwise -> update last appearance
        Return False (no matching)
        """
        last_duplucates = {}

        for i in range(len(nums)):
            last_index = last_duplucates.get(nums[i])

            if last_index is None:
                last_duplucates[nums[i]] = i
            else:
                if i - last_index <= k:
                    return True
                else:
                    last_duplucates[nums[i]] = i

        return False

    # id290 _HashTable
    def wordPattern(self, pattern: str, str: str) -> bool:
        """
        Create matcher for patterns and words
        Split str to separate words
        If count of characters in pattern and words not matched -> return False
        Iterate words:
        If char already in pattern and word from matcher and current word not matched -> return False
        If current word is registered in matcher -> return False
        Otherwise -> register word in matcher
        Return True (all words matched)
        """
        matcher = {}
        i = 0
        words = str.split()

        if len(words) != len(pattern):
            return False

        while i < len(words) and i < len(pattern):
            char = pattern[i]

            if char in matcher:
                right_word = matcher[char]

                if right_word != words[i]:
                    return False
            elif words[i] in matcher.values():
                return False
            else:
                matcher[char] = words[i]

            i += 1

        return True

    # id347 _HashTable _Heap
    # Todo: see heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Count every element with hash table
        Sort hash table with values
        Return last k keys (nums themselves)
        """
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        frequency = {key: value for key, value in sorted(frequency.items(), key=lambda item: item[1])}

        return list(frequency.keys())[-k:]

    # id349 _HashTable _TwoPointers _BinarySearch _Sort
    # Todo: see tp, bs, sort
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Construct set from each list
        Return intersection of two sets
        """
        return list(set(nums1).intersection(set(nums2)))

    # id500 _HashTable
    def findWords(self, words: List[str]) -> List[str]:
        """
        Init keyboard in list
        For every word:
        For every char:
        Get saved row from dict by char of word
        If not saved (i.e. first char) -> save row found
        Otherwise -> compare with saved row
        If not matched -> skip word
        Return saved words
        """
        keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        saved = {}
        result = []

        for word in words:
            save = True

            for char in word:
                row = saved.get(word)

                if row is None:
                    for i in range(len(keyboard)):
                        if char.lower() in keyboard[i]:
                            saved[word] = i
                            break
                else:
                    for i in range(len(keyboard)):
                        if char.lower() in keyboard[i]:
                            if i != saved[word]:
                                save = False
                                break

            if save:
                result.append(word)

        return result

    # id560 _Array _HashTable
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1

        count, _sum = 0, 0

        for num in nums:
            _sum += num
            count += sums[_sum - k]
            sums[_sum] += 1

        return count

    # id599 _HashTable
    # Todo: too slow
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        Count all restaurants appeared in both lists with their sum of indices
        Get minimum sum
        Iterate counter and return restaurant with minimum sum of indices
        """
        counter = {}
        indices = []

        for i, restaurant in enumerate(list1):
            if restaurant in list2:
                counter[restaurant] = i + list2.index(restaurant)

        min_index = min(counter.values())

        for restaurant, index_sum in counter:
            if index_sum == min_index:
                indices.append(restaurant)

        return indices

    # id692 _HashTable _Heap _Trie
    # Todo: see heap, trie
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Count every element with hash table
        Sort hash table with values
        Return first k keys (sort reversed by counts and normal by word)
        """
        frequency = {}

        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        frequency = {key: value for key, value in sorted(frequency.items(), key=lambda item: (-item[1], item[0]))}

        return list(frequency.keys())[:k]

    # id771 _HashTable
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        Create dictionary with values of J
        Iterate over S and check every character in jewels
        If in jewels -> increment count
        Return count
        """
        jewels, count = {}, 0

        for char in J:
            jewels[char] = True

        for char in S:
            if jewels.get(char):
                count += 1

        return count
