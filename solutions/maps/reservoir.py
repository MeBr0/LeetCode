from typing import List


# id398 _ReservoirSampling
class Solution:

    def __init__(self, nums: List[int]):
        """
        Create hash table for storing value with all indices
        If number appeared -> append new index
        Otherwise -> create list with first index
        """
        self.random_pick = {}

        for i in range(len(nums)):
            if nums[i] in self.random_pick:
                self.random_pick[nums[i]].append(i)
            else:
                self.random_pick[nums[i]] = [i]

    def pick(self, target: int) -> int:
        """
        Choose random from all appeared indices
        """
        import random
        return random.choice(self.random_pick[target])
