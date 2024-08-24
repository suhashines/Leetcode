def better(arr):

    longest = float('-inf')

    cnt = 1

    arr.sort()

    n = len(arr)

    for i in range(n):

        if( i!=n-1 and arr[i+1]==arr[i]+1):
            cnt +=1
        else:
            longest = max(longest,cnt)
            cnt = 1
    print(f"longest {longest}")


# better([1,2,4,5,7,8,9])



def optimal(arr):

    st = set(arr)  # O(n)

    # print(st)

    longest = float('-inf')

    for element in st:

        if element-1 not in st:

            cnt = 1

            while element+cnt in st:
                cnt +=1

            longest = max(longest,cnt)

    print(f"longest {longest}")

optimal([1,6,2,7,4,5])