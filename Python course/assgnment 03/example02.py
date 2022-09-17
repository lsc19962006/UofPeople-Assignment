# This example is to determine whether the number (0˜5) input from the user is a prime number #
# In nested conditional way #

n=int(input())

if n < 0 or n > 5:
    print("number you input beyond the allowed value range")
    exit()  # end the program #

if n != 0:
  if n != 1:
    if n != 4:
      print("this is a prime number")
      exit()

print("this is not a prime number")
