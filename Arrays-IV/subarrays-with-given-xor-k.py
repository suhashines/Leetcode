def brute(a,k):

    cnt = 0

    for i in range(len(a)):

        xor = 0

        for j in range(i,len(a)):

            xor ^= a[j]

            if(xor == k): cnt+=1
    print(cnt)

def optimal(a,k):

    '''
    for some i, is there any subarray ending at i with given xor k
    xor up to i = xor up to j ^ k
    xor[i] ^ k = j
    hence there must exist the element j
    '''
    
    xor = cnt = 0

    map = {}

    for i in range(len(a)):

        xor ^= a[i]

        if(xor==k): cnt+=1

        if(xor ^ k in map): cnt+= map[xor^k]

        if(xor in map): map[xor]+=1
        else: map[xor] = 1
    
    print(cnt)


optimal([4, 2, 2, 6, 4],6)