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

    arr.sort()

    n = len(arr)

    for i in range(n):

        print(f"i {i}")

        if(arr[i]<trgt):

            j = binSearch(arr,i+1,n,trgt-arr[i])

            print(j)

            if(j!=-1): return i,j
    
    return None


print(two_sum([3,2,4],6))