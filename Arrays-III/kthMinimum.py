import random

def swap(arr,i,j):

    arr[i],arr[j]=arr[j],arr[i]


def hoare_partition(arr,l,h):

    partition_index = random.randint(l,h-1)

    pivot = arr[partition_index]

    i = l 
    j = h-1

    while(True):

        while(arr[i]<pivot):
            i+=1
        
        while(arr[j]>pivot):
            j-=1
        
        if(i>=j): return j

        swap(arr,i,j)
        i+=1
        j-=1
    
    return j

def partition(arr,l,h):

    pivot_index = random.randint(l,h-1)

    swap(arr,pivot_index,h-1)

    pivot = arr[h-1]

    print(f"pivot index : {pivot_index}")

    pi = l

    while(l!=h):

        if(arr[l]<pivot):

            swap(arr,pi,l)
            pi +=1
        
        l+=1
    swap(arr,pi,h-1) 
    
    return pi


def kthMinimum(arr,l,h,k):

    pi = partition(arr,l,h)

    if(pi-l+1==k): return arr[pi]

    if(pi-l+1<k):
        return kthMinimum(arr,pi+1,h,k-pi+l-1)
    
    return kthMinimum(arr,l,pi,k)

print(kthMinimum( [7, 10, 4, 3, 20, 15],0,6,3))