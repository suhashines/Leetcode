def moore_voting(arr):

    cnt1 = cnt2 = 0

    elem1 = elem2 = -1

    thr = len(arr)//3 + 1

    for i in range(len(arr)):

        if(cnt1==0):
            elem1 = arr[i]
            cnt1 = 1
        elif(cnt2==0):
            cnt2=1
            elem2 = arr[i]

        elif(arr[i]==elem1):
            cnt1+=1
        
        elif(arr[i]==elem2):
            cnt2+=1

        else:
            cnt1-=1
            cnt2-=1
    
    #check the potential answer

    cnt1=cnt2=0

    for i in range(len(arr)):

        if(arr[i]==elem1): cnt1+=1
        elif(arr[i]==elem2): cnt2+=1
    
    l = []

    if(cnt1>=thr): l.append(elem1)

    if(cnt2>=thr): l.append(elem2)

    print(l)


moore_voting([1,2])