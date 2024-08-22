def brute(arr,trgt):

    maxCount = 0

    for i in range(0,len(arr)):

        sum = arr[i]

        if(sum==trgt): maxCount = max(maxCount,1)

        for j in range(i+1,len(arr)):

            sum += arr[j]

            if(sum==trgt): maxCount = max(maxCount,j-i+1)
    print(maxCount)

def optimal(arr):
    # the solution uses the idea of prefix sum
    # if an entire subarray is zero, then the prefix sum before and
    # after the subarray will be same

    map = {}

    longest = sum = 0

    for i in range(len(arr)):

        sum += arr[i]

        if(sum==0): longest = max(longest,i+1)
        elif(sum in map): longest = max(longest,i-map[sum])
        else:
            map[sum] = i

    print(f"longest {longest}")

optimal([0,0,0,0])