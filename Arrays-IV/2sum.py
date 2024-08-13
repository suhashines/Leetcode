def binSearch(arr,l,h,trgt):

    print(f"trgt {trgt}")

    if(l+1==h):

        if(arr[l]==trgt): return l
        return -1
    

    m = (l+h)//2

    if(arr[m]==trgt): return m

    if(arr[m]>trgt):
        return binSearch(arr,l,m,trgt)
    return binSearch(arr,m+1,h,trgt)

def two_sum(arr,trgt):

    tmp = arr

    arr.sort()

    n = len(arr)

    for i in range(n):

        print(f"i {i}")

        if(arr[i]<trgt):

            j = binSearch(arr,i+1,n,trgt-arr[i])

            print(j)

            if(j!=-1): return i,j
    
    return None


def optimal(arr,trgt):

    tmp = []

    for i in range(len(arr)):

        tmp.append([arr[i],i])
    
    

    #sorting the array

    tmp.sort(key=lambda x: x[0])

    print(tmp)

    left = 0
    right = len(tmp)-1

    print(f"right {right}")

    while(left<right):

        if(tmp[left][0]+tmp[right][0]==trgt): return [tmp[left][1],tmp[right][1]]

        elif(tmp[left][0]+tmp[right][0]<trgt):
            left +=1
        else:

            right-=1

    return []

print(optimal([2,5,7,3,8],8))