def binarysearch2 (arr, target):
    lower=0
    upper=len(arr)-1

    while lower <= upper:
        middle=(lower+upper) // 2

        if arr[middle]==target:
            return middle
        else:
            if arr[middle]<target:
                lower=middle+1
            else:
                upper=middle-1
    return -1

print(binarysearch2(input_array, input_target))

testarray=[3,4,5,6,1,2]

def findMin(arr):
    lower=0
    upper=len(arr)-1
    
    while lower > upper:
        middle=(lower+upper)//2
        if arr[middle]<upper and arr[middle]>lower:
            lower=middle+1
        else:
            upper=middle-1