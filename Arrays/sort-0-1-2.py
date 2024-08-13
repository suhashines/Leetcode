def swap(arr,i,j):

    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def sortHelper(arr,key,k):

    for i in range(k,len(arr)):

        if(arr[i]==key):
            swap(arr,i,k)
            k += 1

    return (arr,k)

def sort_0_1_2(arr):

    arr,k = sortHelper(arr,0,0)

    arr,k = sortHelper(arr,1,k)

    arr,k = sortHelper(arr,2,k)

    print(arr)


def dutchNationalFlag(arr):

    m = l = 0 

    h = len(arr)-1

    while(m<=h):

        if(arr[m]==0):

            swap(arr,l,m)
            m += 1
            l += 1
        
        elif(arr[m]==1):
            m += 1
        
        else:
            swap(arr,h,m)
            h -= 1

    print(arr)


sort_0_1_2([0,1,2,0,1,2])