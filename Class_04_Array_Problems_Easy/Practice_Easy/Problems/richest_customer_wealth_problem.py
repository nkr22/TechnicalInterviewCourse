# You are given an m x n integer grid accounts where accounts[i][j]
# is the amount of money the ith customer has in the jth bank.
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

input_accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17

def richcustomer(arr):
    mostwealth=0
    for i in range (0, len(arr)):
        currentcustwealth=0
        for j in range (0,len(arr[i])):
            currentcustwealth+=arr[i][j]
        if currentcustwealth>mostwealth:
            mostwealth=currentcustwealth
    return mostwealth

print(richcustomer(input_accounts))

def richcustomer2(arr):
    mostwealth=0
    for i in range (0, len(arr)):
        currentcustwealth=0
        currentcustwealth=sum(arr[i])
        if currentcustwealth>mostwealth:
            mostwealth=currentcustwealth
    return mostwealth

print(richcustomer2(input_accounts))
