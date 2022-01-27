# Search an array of numbers to find a target number using binary search.
# The function should return the index of the target number if the target number is found
# or a -1 if the target is not found in the array

input_array = [1, 2, 5, 9, 12, 15, 21, 28, 99, 100, 117]
input_target = 5
# pos=-1
# Output = 2

# def binarysearch (arr, n):
#     lower=arr[0]
#     upper=arr[len(arr)-1]

#     while lower <= upper:
#         mid=(lower+upper) // 2 

#         if arr[mid] == n:
#             globals()['pos']=mid
#             return True
#         else:
#             if arr[mid]<n:
#                 lower=mid+1
#             else:
#                 upper=mid-1
#     return False

# print(binarysearch(input_array, input_target))


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