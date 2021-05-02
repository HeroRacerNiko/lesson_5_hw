from Arithmetical_mean import array_1, array_2


def two_lowest(arr_list):
    if len(arr_list) < 2:
        return f'Please make sure list has at least 2 numbers'
    result = [arr_list[0]]
    while len(result) < 2:
        result.append(min(arr_list))
    return result


print(two_lowest(array_1))
print(two_lowest(array_2))
