def bruteForce(arr): # O(n^2)

    max_profit = 0

    for i in range(len(arr)):

        for j in range(i+1,len(arr)):

            profit = arr[j]-arr[i]

            max_profit = max([max_profit,profit])

    print(f"profit: {max_profit}")


def optimal(arr):  # O(n)

    min = float('inf')

    max_profit = 0

    buy_day = sell_day = min_day = 0


    for i in range(len(arr)):

       if(arr[i]<min):
           min_day = i
           min = arr[i]
       
       profit = arr[i]-min

       if(profit>max_profit):
           max_profit = profit
           sell_day = i
           buy_day = min_day


    print(f"Maximum profit: {max_profit}, Buy on day {buy_day}, Sell on day {sell_day}")

bruteForce([4,20,1,2,3,4])
optimal([4,20,1,2,3,4])