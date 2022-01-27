input_array=[3,4,5,6,1,2]

def findMax(arr):
    lower=0
    upper=len(arr)-1
    
    while lower < upper:
        middle=(lower+upper)//2
        if arr[middle]<arr[lower]:
            upper=middle-1
        else:
            lower=middle
    return arr[upper]

print(findMax(input_array))