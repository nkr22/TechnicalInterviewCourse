test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
             'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
             'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}

def sortbymarks(dictionary):
    results={}
    for item in dictionary:
        newvalue=dict(sorted(dictionary[item].items(), key=lambda dict_item: dict_item[1], reverse=False))
        results[item]=newvalue

    return (results)

print(sortbymarks(test_dict))

#stephen's solution
def sortByValues(myDict):
    return {k:dict(sorted(v.items(),key= lambda kv:kv[1])) for k,v in myDict.items()}