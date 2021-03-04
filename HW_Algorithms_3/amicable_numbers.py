from HW_Algorithms_2.HW_Algorithms_2 import divisor_list


def amicable_nums(num1, num2):
    # num1_friendly_to_num2 = False
    # num2_friendly_to_num1 = False
    # amicable = False
    # if sum(divisor_list(num1)) == num2:
    #     num1_friendly_to_num2 = True
    # if sum(divisor_list(num2)) == num1:
    #     num2_friendly_to_num1 = True
    # if num1_friendly_to_num2 and num2_friendly_to_num1:
    #     amicable = True
    # return amicable

    if sum(divisor_list(num1)) == num2 and sum(divisor_list(num2)) == num1:
        return True


print(amicable_nums(220, 284))
