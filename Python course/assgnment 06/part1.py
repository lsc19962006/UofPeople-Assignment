import math
def my_sqrt(a):
    x=math.ceil(a/2)
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
    return y

a=int(input())
print(my_sqrt(a))
