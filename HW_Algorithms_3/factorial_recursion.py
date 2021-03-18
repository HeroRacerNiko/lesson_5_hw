# Multiply number to subsequent numbers all the way to 1
# Stopping case as number hits 1
# Keep multiplying number by (number itself -1) until hit 1


def factorial(num):
    if num < 0:
        return "Positive numbers only"
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)


# print(factorial(4))


