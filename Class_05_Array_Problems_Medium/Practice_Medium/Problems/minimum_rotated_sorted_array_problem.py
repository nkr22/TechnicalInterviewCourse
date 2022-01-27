# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand. You may assume no duplicate exists in the array.
# This problem came from leetcode.com

input_array = [3, 4, 5, 6, 1, 2]
# Output = 1

def findMin(arr):
    lower=0
    upper=len(arr)-1
    
    while lower < upper:
        middle=(lower+upper)//2
        if arr[middle]>arr[upper]:
            lower=middle+1
        else:
            upper=middle
    return arr[lower]

print(findMin(input_array))