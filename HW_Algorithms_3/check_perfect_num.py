from HW_Algorithms_2.HW_Algorithms_2 import divisor_list


def is_perfect(num):
    if num == 0:
        return False
    if sum(divisor_list(num)) == num:
        return True
    return False


# print(is_perfect(6))
# print(is_perfect(28))
# print(is_perfect(496))
# print(is_perfect(8128))
# print(is_perfect(5))
# print(is_perfect(0))
# print(is_perfect(1))
# print(is_perfect(6788))
