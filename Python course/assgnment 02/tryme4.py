def new_line():
    print('.')

def three_lines():  # call new_line function to print 3 lines #
    new_line()
    new_line()
    new_line()

def nine_lines():  # call three line in 3 times make it print nine lines. #
    three_lines()
    three_lines()
    three_lines()

def clear_screen():  # call nine_lianes, three_lines and new_line funtion make it print 25 lines. #
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

# main funtion below #

nine_lines()
print("next funtion")
clear_screen()