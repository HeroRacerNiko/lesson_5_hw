# If number is bigger than 10
# keep adding (remainder of num divided by 10) and (absolute division of num //) and updating num with that sum
# until sum of two nums make a number less than 10

def dig_root(num):
    if num < 10:
        return num
    else:
        num = (num % 10) + (num // 10)
    return dig_root(num)


# print(dig_root(23657))


def dig_root_str(num):
    while len(str(num)) > 1:
        temp = 0
        for char in str(num):
            temp += int(char)
        num = temp
    return num


# print(dig_root_str(23657))
