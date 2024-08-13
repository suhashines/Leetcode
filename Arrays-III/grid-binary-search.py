def optimal(mat,rl,rh,cl,ch,target):

    if(rl+1==rh and cl+1==ch):

        if(mat[rl][cl]==target):
            return True
        return False

    if(cl+1==ch):

        rm = (rl+rh)//2
        if(mat[rm][cl]==target): return True
        elif(mat[rm][cl]>target): return optimal(mat,rl,rm,cl,ch,target)
        return optimal(mat,rm+1,rh,cl,ch,target) 
    
    if(rl+1==rh):

        cm = int((cl+ch)/2)

        if(mat[rl][cm]<target):
            return optimal(mat,rl,rh,cm+1,ch,target)
        elif(mat[rl][cm]>target):
            return optimal(mat,rl,rh,cl,cm,target)
        return True 

    rm = int((rl+rh)/2)
    cm = int((cl+ch)/2)

    if(mat[rm][cm]<target):
        return optimal(mat,rm,rh,cl,ch,target)
    elif(mat[rm][cm]>target):
        return optimal(mat,rl,rm,cl,ch,target)
    else:
        return True
    

matrix = [[1],[2],[3],[4],[5],[6],[7],[8]]
print(optimal(matrix,0,8,0,1,10))