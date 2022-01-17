#find min and max array
test=[1,5,6,8,2,3]

def minmax (arr):
    min=arr[0]
    max=arr[0]
    for i in range(0, len(arr)):
        if arr[i]<min:
            min=arr[i]
        if arr[i]>max:
            max=arr[i]
    return max, min

print(minmax(test))