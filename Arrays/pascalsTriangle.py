import collections

def pascalsTriangle(rows):

    p = []

    p.append(collections.deque([1]))

    if(rows==1): return p

    p.append(collections.deque([1,1]))

    if(rows==2): return p

    for i in range(2,rows):

        ll = collections.deque([1,1])

        for j in range(i-1):

            ll.insert(j+1,p[i-1][j]+p[i-1][j+1])
            print(ll)
        
        p.append(ll)
    
    print(p)


pascalsTriangle(5)