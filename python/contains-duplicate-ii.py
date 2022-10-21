def containsNearbyDuplicate(nums, k):
    for idx, numI in enumerate(nums):
        indexI = idx
        for idx, numJ in enumerate(nums):
            indexJ = idx
            if numI == numJ and indexI != indexJ and abs(indexI - indexJ) <= k:
                return True
    return False


    

print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
