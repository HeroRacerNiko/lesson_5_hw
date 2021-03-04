"""
Initiate default values as [0, 1];
Check number for 0, if 0 = return 0;
Check number for 1 or 2, if true = return 1;
Call function itself with (-1) + (-2) until function hits edge cases of length of result
Return the result of above call stack
"""


def fib(num):
    result = [0, 1]
    if num == 0:
        return 0
    elif num < 0:
        return 'Invalid input, number must be positive'
    elif num <= len(result):
        return result[-1]
    else:
        return fib(num - 1) + fib(num -2)


# print(fib(0))
# print(fib(-1))
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(8))
