# function accepts only whole numbers at this point.
# float() needs to be correctly inserted to check for floating numbers.
# Possibly use try/expect/else

def find_max():
    # make sure all inputs are numeric inputs, otherwise infinite promp asking for a number
    num1 = input('Enter the first whole number: ')
    while not num1.isnumeric():
        num1 = input('Enter number in DIGITS: ')

    num2 = input('Enter the second whole number: ')
    while not num2.isnumeric():
        num2 = input('Enter the number in DIGITS: ')

    num3 = input('And...finally, enter the third whole number: ')
    while not num3.isnumeric():
        num3 = input('Enter the number in DIGITS: ')

    return max(num1, num2, num3)


print(find_max())
