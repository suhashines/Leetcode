def optimal(nums):

    n = len(nums)
    sum = 0
    square_sum = 0

    for i in range(n):
        sum+= nums[i]
        square_sum += nums[i]*nums[i]
    
    

    natural_sum = (n*(n+1))/2

    natural_square_sum = (n*(n+1)*(2*n+1))/6

    a = square_sum - natural_square_sum  # x^2 - y^2

    b = sum - natural_sum   # x - y

    repeated = int(((a/b) + b)/2)

    missing = int(((a/b) - b)/2)

    print(f"repeated:{repeated} missing:{missing}")


optimal([4,3,6,2,1,1])