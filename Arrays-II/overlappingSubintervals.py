def optimal(mat):

    ans = []

    # good practice to sort the intervals

    mat.sort(key=lambda x:x[0])

    # overlapping logic
    
    prev_start = mat[0][0]
    prev_end = mat[0][1]

    for i in range(1,len(mat)):

        if(mat[i][0] <= prev_end):

            prev_end = max(prev_end,mat[i][1])
        else:

            ans.append([prev_start,prev_end])
            prev_start = mat[i][0]
            prev_end = mat[i][1]
    
    ans.append([prev_start,prev_end])

    print(ans)

optimal([[4,5],[1,4]])