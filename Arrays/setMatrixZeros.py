def optimal(mat):

    rows = len(mat)
    columns = len(mat[0])
    col_0 = -1
    for i in range(rows):

        for j in range(columns):

            if(mat[i][j]==0):

                if(j==0):
                   col_0 = 0
                else:
                    mat[i][0] = 0
                    mat[0][j] = 0

    for i in range(1,rows):

        for j in range(1,columns):

            if(mat[i][0]==0 or mat[0][j]==0): mat[i][j]=0

    for i in range(1,columns):
        if(mat[0][0]==0):
            mat[0][i] = 0

    for i in range(1,rows):

        if(col_0 == 0): mat[i][0]=0

    print(mat)

optimal([])