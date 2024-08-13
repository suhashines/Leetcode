def pow(x,n):

    if(n==0): return 1

    if(n%2==1):
        return x*pow(x,n-1)
    else:
        n = n//2
        temp = pow(x,n)
        return temp*temp


print(pow(2,10))