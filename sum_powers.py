


"""
File: sum_powers.py
Copyright (c) 2016 Lisa Dong
License: MIT
-asks user for a floating point number (b) and a natural number (n)
-computes the sum of 1 + b + b^2 + ... + b^n
-prints the sum
"""


bstring = raw_input("enter a floating point number: ")
b = float (bstring)

nstring = raw_input("enter a natural number: ")
n = int (nstring)

i = 0
sum = 0

while i<=n:

    sum += b**i*1.0
    
    i +=1


print sum

part2 = b**(n+1)/(b-1)

print part2
