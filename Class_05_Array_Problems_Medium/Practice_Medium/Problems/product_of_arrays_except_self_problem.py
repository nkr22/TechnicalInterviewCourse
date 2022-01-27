# Given an array nums of n integers where n > 1, return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i]
# Note: Please solve it without division
# This problem came from leetcode.com

input_array = [1, 2, 3, 4]
# Output = [24, 12, 8, 6]

def productarray(arr):
    productarray=[]
    for num1 in range(0, len(arr)):
        product=1
        for num2 in range(0, len(arr)):
            if num2 != num1:
                product=product*arr[num2]
        productarray.append(product)
    return productarray

print(productarray(input_array))