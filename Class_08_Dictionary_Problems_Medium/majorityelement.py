test_array=[3,2,3]
test_array2=[2,2,1,1,1,2,2]

def majorityelement(arr):
    countdict={}
    for item in arr:
        if item in countdict:
            countdict[item]+=1
        else:
            countdict[item]=1
    
    for key in countdict:
        if countdict[key]>(len(arr)/2):
            return key

print(majorityelement(test_array))
print(majorityelement(test_array2))

    