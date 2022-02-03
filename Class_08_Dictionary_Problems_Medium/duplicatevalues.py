test_dict = {'Manjeet' : [1, 4, 5, 6],
			'Akash' : [1, 8, 9],
			'Nikhil': [10, 22, 4],
			'Akshat': [5, 11, 22]}

def duplicatevalues(dict):
    count={}
    for i in dict:
        for j in dict[i]:
            if j in count:
                count[j]+=1
            else:
                count[j]=1
    
    for key in count:
        if count[key]>1 :



    return (results)