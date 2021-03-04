# Fibonacci sequence
def fib(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1

    result = [1, 1]
    i = 0
    while i < num - 2:
        result.append(int(result[-1]) + int(result[-2]))
        i += 1
    # return *result,
    return result


# print(fib(4))
# print(fib(10))


def zeros(num):
    num = str(num)
    i = 0
    while i < len(num):
        if num[-1] == '0':
            num = num[:-1]
        i += 1
    return num


# print(zeros(300400))
# print(zeros(3400))


# Recursive digits of num sum

def rec_sum_of_digits(num):
    result = 0
    if len(str(result)) == 1 and result != 0:
        return result
    num = str(num)

    for ele in num:
        result += int(ele)

    print(result)

    if len(str(result)) == 1:
        return result
    else:
        return rec_sum_of_digits(result)


# print(rec_sum_of_digits(11188822287))
# print(rec_sum_of_digits(132189))


def highest_common_divisor(n1, n2):
    result = []
    i = 1
    while i <= max(n1, n2):
        if n1 % i == 0 and n2 % i == 0:
            result.append(i)
        i += 1
    # return *result,
    return result[-1]


# print(highest_common_divisor(24, 56))
# print(highest_common_divisor(20, 86))

def divisor_list(n):
    result = []
    i = 1
    while i < n:
        if n % i == 0:
            result.append(i)
        i += 1
    return result

