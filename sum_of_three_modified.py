from random import randint


def sum_of_three(n):
    # Check if input is numeric, otherwise ask to re-enter
    while not n.isnumeric():
        n = input('Please enter a NUMBER: ')
    # Check if number is greater then 0
    while int(n) <= 0:
        n = input('Please enter a POSITIVE number: ')
    result = 0
    result_str = ''
    random_number = randint(0, int(n))
    print(f'User input is: {n}')
    print(f'Random number is: {random_number}')
    for char in str(random_number):
        result += int(char)
        if result_str == '':
            result_str += char
        else:
            result_str += f' + {char}'
    print(f'Breaking down the random number into individual digits...')
    return f'{result_str} = {result}'


print(sum_of_three(input('Please enter a positive number: ')))



