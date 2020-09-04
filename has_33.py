def has_33(nums):
    for x in range(len(nums)):
        # if nums[x] == 3 and nums[x+1] == 3:
        if nums[x:x + 2] == [3, 3]:
            return True
    return False


print(has_33([1, 3,1, 3,3]))
