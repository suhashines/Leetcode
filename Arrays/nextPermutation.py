nums = [1,2,3,4] 

def nextPermutation(nums):

    length = len(nums)

    left = right = []

    min_index = -1 

    min_value = float('inf')

    for i in range(length-2,-1,-1):

        for j in range(i+1,len(nums)):

            if nums[j]> nums[i] and nums[j]<min_value:

                min_index = j
                min_value = nums[j]
                # print(f"min_index set to {j}")

        if(min_index!=-1):
            temp = nums[i]
            nums[i]=nums[min_index]
            nums[min_index]=temp
            left = nums[:i+1]
            right = nums[i+1:]
            break        


    if(min_index==-1):

        nums.sort()
    else:

        # print(f"left : {left} , right: {right}, pivot: {nums[pivot_index]} ")
        
        right.sort()

        nums = left+right

    return nums

print(nextPermutation(nums))