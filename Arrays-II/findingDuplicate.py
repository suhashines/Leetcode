def linkListCycleMethod(nums):

    slow = nums[0]
    fast = nums[nums[0]]

    while(slow!=fast):
        slow = nums[slow]
        fast = nums[nums[fast]]
        print(f"slow: {slow} , fast: {fast} ")
    
    slow = 0

    while(slow!=fast):

        slow = nums[slow]
        fast = nums[fast]

        print(f"slow: {slow} , fast: {fast} ")
    
    return slow


print(linkListCycleMethod([1,2,3,4,5,6,6]))