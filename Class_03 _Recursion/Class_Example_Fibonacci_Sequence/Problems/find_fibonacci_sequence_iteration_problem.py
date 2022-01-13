# Write a program that creates a portion of the fibonacci sequence iteratively

def fibonacci (n):
    if n<=1 :
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


print(fibonacci(14))