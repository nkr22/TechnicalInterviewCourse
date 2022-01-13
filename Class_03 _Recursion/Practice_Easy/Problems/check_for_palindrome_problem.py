# Write a function that checks if a string is a palindrome using recursion

def palindrome (string):
    if string=="" or len(string)==1 :
        return True
    if string[0]!=string[-1]:
        return False
    else:
        string=string[1:-1]
        return palindrome(string)

print(palindrome('abcba'))