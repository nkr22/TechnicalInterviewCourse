test_array=2,7,11,15
target=9

test_array2=[10,-5,6,14]
target1=9


def twosum(arr, target):
    sumdict={}
    for index, num in enumerate(arr):
        sumdict[num]=index
    for element in sumdict:
        if (target-element) in sumdict:
            return (sumdict[element], sumdict[target-element])

print(twosum(test_array, target))
print(twosum(test_array2, target1))


# Spencer's solution in class
# nums1 = [2, 7, 11, 15]
# # const target1 = 9

# nums2 = [3,2,4]
# # const target2 = 6

# nums3 = [3, 2]
# # const target3 = 6


# def two_sum (arr, target) :
#     dic = {}
#     for i, j in enumerate(arr) :
#         needed_num = target - j
#         if needed_num in dic : return [dic[needed_num], i]
#         else : dic[j] = i

# print(two_sum(nums1, 26))