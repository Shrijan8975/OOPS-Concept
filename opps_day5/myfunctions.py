def sum(x,y):
    return x + y

def fact(n):
    f =1
    while(n>=1):
        f = f * n
        n = n -1
    return f

def sumofdigits(n):
    sum = 0
    while(n != 0):
        sum += n%10
        n //=10
    return sum