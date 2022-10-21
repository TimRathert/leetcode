def containsNearbyDuplicate(nums, k):
    for idx, numI in enumerate(nums):
        indexI = idx
        for idx, numJ in enumerate(nums):
            indexJ = idx
            if numI == numJ:
                if indexI - indexJ <= k:
                    return True
    return False


    

print(containsNearbyDuplicate([1,2,3,1], 3))