array_1 = [1, 2, 3, 4, 5, 6]
array_2 = [45, 67, 78, 99, 2]


# Two function solution (helper function)
# def arith_mean(arr_list):
#     return sum(arr_list) / len(arr_list)
#
#
# def return_list_of_nums_less_then_arith_mean(arr_list):
#     result_list = []
#     for num in arr_list:
#         if num < arith_mean(arr_list):
#             result_list.append(num)
#
#     return result_list


# Version 2 (single function solution)
def return_list_of_nums_less_then_arith_mean(arr_list):
    result_list = []
    arith_mean = sum(arr_list) / len(arr_list)
    for num in arr_list:
        if num < arith_mean:
            result_list.append(num)

    return result_list


# print(return_list_of_nums_less_then_arith_mean(array_1))
# print(return_list_of_nums_less_then_arith_mean(array_2))


