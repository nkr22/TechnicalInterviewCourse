input_arr=[10, 3, 5, 6, 20]

#Output is 1200

def merge_sort(arr):
    merge_sort2(arr, 0, len(arr)-1)

def merge_sort2(arr, first, last):
    if first<last:
        middle=(first+last)//2
        merge_sort2(arr, first, middle)
        merge_sort2(arr, middle+1, last)
        merge(arr, first, middle, last)

def merge(arr, first, middle, last):
    left = arr[first:middle+1]
    right = arr[middle+1:last+1]
    left.append(999999999)
    right.append(999999999)
    i=0
    j=0

    for k in range()

maxproduct=arr[-1]*arr[-2]*arr[-3]