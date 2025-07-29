# Sum of first odd numbers till n without Loop
# import math 
from math import ceil as c
n = int(input("Enter the value n: "))
#if(n%2  != 0):
#    n = n+1 
print("Sum of odd numbers till %d is %d"%(n,c(n/2)**2))