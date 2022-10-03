import math
def my_sqrt(a):
    x=math.ceil(a/2)
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
    return y

a=1
while a<=25:
    print("a=" + str(a) + " | my_sqrt(a) = " + str(my_sqrt(a))+ " | math.sqrt(a) = " + str(math.sqrt(a)) + " | diff = " + str(abs(math.sqrt(a)-my_sqrt(a))))
    a+=1