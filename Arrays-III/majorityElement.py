def moore_voting(arr): # find the element that appears more than n/2

    thr = len(arr)//2
    cnt = i = 0
    elem = -1
    for i in range(len(arr)):

        if(cnt==0):
            elem = arr[i]

        if(arr[i]==elem): cnt+=1

        else: cnt-=1

    cnt = 0

    for i in range(len(arr)):

        if(arr[i]==elem): cnt+=1

    if(cnt>thr): return elem

    return -1

arr = [2, 2, 1, 1, 2, 2, 2]
print(f"Majority element: {moore_voting(arr)}")