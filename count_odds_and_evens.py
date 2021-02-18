# Function check only WHOLE number
# Function doesn't check for digits duplication in the parameter number input
# For example 44411 would return 3 even digits and 2 odds
# Function does NOT skip count with duplicate digit and will count and add to list of evens or odds

def count_odds_and_evens(num):
    while not num.isnumeric():
        num = input('Please enter a whole number with DIGITS: ')
    evens = []
    odds = []
    for char in num:
        if int(char) % 2 == 0:
            evens.append(char)
        else:
            odds.append(char)
    print(evens)
    return f'In {num} there are {len(evens)} even digits {*evens,} and {len(odds)} odd digits {*odds,}'


# print(count_odds_and_evens(input('Enter a number: ')))

# helper function
def prettify_dict(obj):
    result = ""
    for key_val in obj:
        result += f'Number {key_val}, count: {obj[key_val]}\n'
    return result

# And following is more sophisticated function that will count evens and odds without duplicating
# the numbers that already occurred. It will also calculate total count of evens and odds.


def count_evens_odds_duplicate_free(n):
    while not n.isnumeric():
        n = input("Enter a whole number in digits: ")
    evens = {}  # local scope variable within function
    odds = {}   # local scope variable within function
    for char in n:
        if int(char) % 2 == 0:
            if char in evens:
                evens[char] += 1
            else:
                evens[char] = 1
        else:
            if char in odds:
                odds[char] += 1
            else:
                odds[char] = 1

    return f'Number {n} has {len(evens)} duplicate free even digits: {*evens,} ' \
           f'\nwith total of {sum(evens.values())} occurrences of even digits ' \
           f'\nList of even digits: \n{prettify_dict(evens)}\n\n' \
           f'Number {n} also has {len(odds)} duplicate free odd digits: {*odds,} ' \
           f'\nwith total of {sum(odds.values())} occurrences of even digits ' \
           f'\nList of even digits: \n{prettify_dict(odds)}'


print(count_evens_odds_duplicate_free(input('Enter a number: ')))

