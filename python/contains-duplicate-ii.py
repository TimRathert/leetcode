def containsNearbyDuplicate(nums, k):
    seen = {}
    for num in nums:
        try:
            seen[num] += 1
        except KeyError as error:
            seen[num] = 1
    print(seen)

containsNearbyDuplicate([1,2,3,1], 3)