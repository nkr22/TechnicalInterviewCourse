# Say you have an array for which the ith element is the price of a given stock on day i
# If you were only permitted to complete at most one transaction (i.e, buy one and 
# sell one share of the stock) design an algorithm to find the maximum profit
# This problem came from leetcode.com

input_array = [7, 1, 5, 3, 6, 4]
# Output = 5

def buystock (arr):
    highprofit=0
    for i in range(0, len(arr)):
        for j in range (i+1, len(arr)):
            profit=arr[j]-arr[i]
            if profit>highprofit:
                highprofit=profit
    return highprofit

print(buystock(input_array))

def buystock2 (arr):
   if len(arr) == 0:
        return 0
    
    min = arr[0]
    maxProfit = 0
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] - min > maxProfit:
            maxProfit = arr[i] - min

    return maxProfit
