from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:

    # id55 _Array _Greedy
    def canJump(self, nums: List[int]) -> bool:
        power = nums[0]

        for i in range(1, len(nums)):
            power -= 1

            if power < 0:
                return False

            if nums[i] > power:
                power = nums[i]

        return power >= 0

    # id45 _Array _Greedy
    def jump(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return 0

        power, power2, count = nums[0], -1, 1

        for i in range(1, length):
            power -= 1

            if power2 != -1:
                power2 -= 1

            if power < 0:
                count += 1
                power = power2
                power2 = -1

            if nums[i] > power and nums[i] > power2:
                power2 = nums[i]

        if power < 0:
            count += 1

        return count

    # id605 _Array _Greedy
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        if length == 1:
            if n == 0:
                return True
            elif n == 1:
                return flowerbed[0] == 0
            else:
                return False

        for i in range(length):
            if i == 0:
                if flowerbed[i] == flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
            else:
                if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1

        return n == 0

    # id860 _Greedy
    # Todo: see greedy, for now stay here
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Create dictionary with count of bills
        For every bill in bills ->
            If change cannot be given -> return false
        Return true (all bills can be given change)
        """
        money, price = {5: 0, 10: 0, 20: 0}, 5

        def get_change(bill: int):
            """
            Add bill to dict money
            Calculate change
            Count how many 10-bill can be constructed from change
            If enough in money -> remove that count from money and take away it from change
            Count how many 5-bill can be constructed from change
            If enough in money -> remove that count from money and take away it from change
            If change is zero -> change can be given
            Otherwise -> cannot
            """
            money[bill] += 1
            change = bill - price

            whole_10 = change // 10
            if money[10] >= whole_10:
                money[10] -= whole_10
                change -= whole_10 * 10

            whole_5 = change // 5
            if money[5] >= whole_5:
                money[5] -= whole_5
                change -= whole_5 * 5

            return change == 0

        for item in bills:
            if not get_change(item):
                return False

        return True
