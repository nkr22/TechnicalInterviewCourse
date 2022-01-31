def uncommon(string1, string2):
    string1=string1.split(' ')
    string2=string2.split(' ')

    wordDict={}
    answer=[]

    for word in string1:
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word]=1
    for word in string2:
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word]=1
    for word in wordDict:
        if wordDict[word]==1:
            answer.append(word)
    return answer



string1="this apple is sour"
string2="this apple is sweet"
print(uncommon(string1, string2))