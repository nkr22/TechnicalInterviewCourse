#find the missing number in an array

test=[1,2,3,5]
test2=[867,868,869,871,872]
def missingnum(arr):
    min=arr[0]
    #max=arr[-1]
    for i in range(0,len(arr)):
        if arr[i]!=min+i:
            missingnum=min+i
            return missingnum

print(missingnum(test))
print(missingnum(test2))

def missingnum2(arr):
    counter=0
    countertocompare=1
    while counter <len(arr):
        if arr[counter] != countertocompare:
            return countertocompare
        countertocompare+=1
        counter+=1

