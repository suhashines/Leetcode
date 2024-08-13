def mergeAndCount(a,l,h):

    m = int((l+h)/2)

    left = a[l:m]
    ll = m-l
    right = a[m:h]
    rl = h-m
    k = l

    i = j = cnt = 0

    while(i<ll and j<rl):

        if(left[i]>right[j]):

            cnt += ll - i
            a[k] = right[j]
            j+=1 
        else:
            a[k] = left[i]
            i+=1
         
        k+=1
    
    while(i<ll):

        a[k] = left[i]
        i+=1
        k+=1

    while(j<rl):

        a[k] = right[j]
        j+=1
        k+=1
    
    return cnt


def inversionCount(a,l,h):

    if(l+1==h):
        return 0
    
    m = int((l+h)/2)

    left_inv = inversionCount(a,l,m)
    right_inv = inversionCount(a,m,h)

    merge_inv = mergeAndCount(a,l,h)

    return left_inv + right_inv + merge_inv

# mergeAndCount([ 5,7,9,2,6,10],0,6)

print(inversionCount([5,4,3,2,1],0,5))