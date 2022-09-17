# This example is to determine whether the number (0˜5) input from the user is a prime number #

# In chained conditional way #
n=int(input())

if n == 2:
    print("this is a prime number")
elif n == 3:
    print("this is a prime number")
elif n == 5:
    print("this is a prime number")
elif n < 0:
    print("number you input beyond the allowed value range")
elif n > 5:
    print("number you input beyond the allowed value range")
else:
    print("this is not a prime number")