# Given an integer n, return True if it is a power of 2. 
# An integer n is a power of two, if there exists an integer x such that n == 2^x

# Examples:
#1,2,4,8,16,32,64

#4=2*2
#32=16*2

#if n=1, output=true, 2^0=1
# 
# Input: n = 4
# Output: True
# 2^2 = 4

# Input : n = 16
# Output : True
# 2^4 = 16

# Input : n = 13
# Output : False

def power_of_n (n):
    if n==1 or n==2:
        return True
    elif n<2:
        return False
    else:
        n=n/2
        return power_of_n(n)

print(power_of_n(8))
