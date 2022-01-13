# Write a function that reverses a string using recursion

def reverse(n) :
    if n=="":
        return ""
    else:
        return reverse(n[1:])+n[0]