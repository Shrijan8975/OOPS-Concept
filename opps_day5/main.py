'''
import myfunctions

n = int(input("Enter number: "))
print("Result: ",myfunctions.fact(n))


import myfunctions as fun

n = int(input("Enter number: "))
print("Result: ",fun.fact(n))
print("Result: ",fun.sumofdigits(n))


from myfunctions import fact,sumofdigits

n = int(input("Enter number: "))
print("Result: ",fact(n))
print("Result: ",sumofdigits(n))

'''

from myfunctions import *

n = int(input("Enter number: "))
print("Result: ",fact(n))
print("Result: ",sumofdigits(n))
