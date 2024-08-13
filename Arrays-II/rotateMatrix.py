def swap(mat,a_row,a_col,b_row,b_col):

    temp = mat[a_row][a_col]

    mat[a_row][a_col] = mat[b_row][b_col]

    mat[b_row][b_col] = temp


def rotateClockwise(mat):

    row = col = len(mat)

    i = 0
    j = row-1

    while(i<=j):

        for k in range(col):

            swap(mat,i,k,j,k)
        i+=1
        j-=1
    
    #print(mat)

    # after swapping we got the diagonal

    for i in range(row):

        for j in range(i+1,col):

            swap(mat,i,j,j,i)

    print(mat)

rotateClockwise([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])