import math


x = 1.55
y = -1.55
# get the largest integer less than x
print(math.floor(x)) # 1
print(math.floor(y)) # -2
# get the smallest integer greater than x
print(math.ceil(x)) # 2
print(math.ceil(y)) # -1
# drop fractional part of x
print(math.trunc(x)) # 1, equivalent to math.floor for positive numbers
print(math.trunc(y))  # -1, equivalent to math.ceil for negative numbers

#Redondear
print(round(1.3)) # 1.0
print(round(0.5)) # 1.0
print(round(1.5)) # 2.0



