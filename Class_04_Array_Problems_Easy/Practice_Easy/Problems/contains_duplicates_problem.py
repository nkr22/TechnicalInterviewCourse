# Given an array of integers, find if the array contains any duplicates
# Your function should return false if every element is distinct.
# This problem came from leetcode.com

input_array = [1, 2, 3, 3, 4]
# Output = True

def containsduplicates(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]==arr[j]:
                return True
    return False

print(containsduplicates(input_array))

def containsduplicates2(arr):
    numbers = []
    for i in range(0, len(arr)):
        if arr[i] in numbers:
            return True
        numbers.append(arr[i])
    return False