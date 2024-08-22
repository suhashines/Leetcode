def better(arr,trgt): # O(n), O(nlogn)

    ans = set()

    for i in range(len(arr)):

        map = {}

        for j in range(i+1,len(arr)):

            print(f"i {arr[i]}, j {arr[j]}")

            key = trgt-(arr[i]+arr[j])

            if key in map:

                tmp = [arr[i],arr[j],key]
                tmp.sort()
                ans.add(tuple(tmp))

            map[arr[j]] = j

    print(ans)


def optimal(arr,trgt): # same complexity but without using extra space

    ans = set()

    for i in range(len(arr)):

        arr[i+1:] = sorted(arr[i+1:])

        l = i+1
        r = len(arr)-1

        while(l<r):

            if(arr[l]+arr[r]==trgt-arr[i]):

                lst = [arr[i],arr[l],arr[r]]
                lst.sort()
                ans.add(tuple(lst))
                l+=1

            elif(arr[l]+arr[r]>trgt-arr[i]):
                r -=1
            else:
                l+=1

    print(ans)

optimal([-1,0,1,2,-1,-4],0)