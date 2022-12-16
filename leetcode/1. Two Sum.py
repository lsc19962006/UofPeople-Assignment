# define the function to draw a heart
def draw_heart():
  # draw the top half of the heart
  for y in range(12, -12, -1):
    for x in range(-15, 16):
      if (x*x + y*y - 225)**3 - x*x*y*y*y <= 0:
        print("*", end="")
      else:
        print(" ", end="")
    print()

  # draw the bottom half of the heart
  for y in range(-11, 12):
    for x in range(-15, 16):
      if (x*x + y*y - 225)**3 - x*x*y*y*y <= 0:
        print("*", end="")
      else:
        print(" ", end="")
    print()

# call the function to draw the heart
draw_heart()