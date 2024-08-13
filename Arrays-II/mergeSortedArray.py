def optimal(nums1,nums2):

    n = len(nums2)
    m = len(nums1)-n
    
    # shifting all the zeros to the right

    for i in range(m-1,-1,-1):
        nums1[i+n] = nums1[i]
        nums1[i]=0
    # print(nums1)

    l = n
    r = 0
    k = 0

    while(l < len(nums1) and r < len(nums2)):

        if(nums1[l]<=nums2[r]):
            nums1[k] = nums1[l]
            l+=1
        else:

            nums1[k] = nums2[r]
            r+=1

        k+=1
    
    while(l<len(nums1)):
        nums1[k]=nums1[l]
        l+=1
        k+=1

    while(r<len(nums2)):
        nums1[k]=nums2[r]
        r+=1
        k+=1

    print(nums1)


optimal([1,2,3,10,0,0,0],[4,5,70]) 