from collections import defaultdict

from torch import true_divide

def containsDuplicates(nums):
    seen = defaultdict(int)
    for i,num in enumerate(nums):
        if num in seen:
            return True
        seen[num] = i
    return False
