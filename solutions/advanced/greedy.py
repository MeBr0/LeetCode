from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    # id860 _Greedy
    # Todo: see greedy, for now stay here
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Create dictionary with count of bills
        For every bill in bills:
        Add bill to dict money
        Calculate change
        Count how many 10-bill can be constructed from change
        If enough in money -> remove that count from money and take away it from change
        Count how many 5-bill can be constructed from change
        If enough in money -> remove that count from money and take away it from change
        If change is zero -> change can be given
        Otherwise -> cannot
        If change cannot be given -> return False
        If all bills can be given change -> return True
        """
        money, price = {5: 0, 10: 0, 20: 0}, 5

        def get_change(bill: int):
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
