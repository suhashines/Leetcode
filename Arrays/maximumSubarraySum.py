def maxSubArraySum(arr):

    maximum = sum = 0

    start_index = end_index = temp = -1

    for i in range(len(arr)):
            
        if(sum+arr[i]<0):
            sum = 0
            temp = i+1
        else:
            sum += arr[i]
            if(sum>maximum):
                maximum = sum
                end_index = i
                start_index = temp

    return (maximum,start_index,end_index)

arr = [-1,-2,-3,-4] 

maximum,si,ei = maxSubArraySum(arr)

print(f"maximum: {maximum},si: {si},ei: {ei}")
