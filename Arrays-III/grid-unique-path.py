def factorial(m,n):

    fact1 = fact2 = ans = 1

    for i in range(1,m+n-1):

        ans *= i

        if(i==m-1):
            fact1 = ans
        if(i==n-1):
            fact2 = ans

    return ans,fact1,fact2

def grid_unique_path(m,n):

    ans,fact1,fact2 = factorial(m,n)

    paths = ans//(fact1*fact2) 

    print(paths)

grid_unique_path(3,5)