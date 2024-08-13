def mergeAndCount(a,l,h):

    m = (l+h)//2

    left = a[l:m]
    ll = m-l
    right = a[m:h]
    rl = h-m
    k = l

    #counting code
    count = 0
    r = m

    print(f"low {l}, high {h}") 

    while(l<m and r<h):

        if(a[l]>2*a[r]):
            count += m-l
            r+=1
        else:
            l+=1

    # merging code
    

    i = j = 0

    while(i<ll and j<rl):

        if(left[i]>right[j]):
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

    print(f"merged {a} , rev {count}")
    return count

    
def reverseCount(a,l,h): # find all the pairs i,j such that i<j and a[i]>2*a[j]

    if(l+1==h):
        return 0
    
    m = (l+h)//2

    lc = reverseCount(a,l,m)
    rc = reverseCount(a,m,h)

    mc = mergeAndCount(a,l,h)

    return lc+rc+mc

print(reverseCount([2,4,3,5,1],0,5))