from longest_word_from_string import phrase
from irreegular_string_to_regular import normalize_string


def find_replace(string, to_be_replaced, to_be_replaced_with):
    # string = normalize_string(string)
    result = ''
    if len(to_be_replaced) == 1:
        for char in string:
            if char == to_be_replaced:
                result += to_be_replaced_with
            else:
                result += char
    else:
        while to_be_replaced in string:
            if string.count(to_be_replaced) > 1:
                result += string[:string.index(to_be_replaced)] + to_be_replaced_with
                string = string[string.index(to_be_replaced) + len(to_be_replaced)::]
            else:
                result += string[:string.index(to_be_replaced)] + to_be_replaced_with + string[string.index(to_be_replaced) + len(to_be_replaced)::]
                string = string[string.index(to_be_replaced) + len(to_be_replaced)::]
    return result


replace_substring = input('Type in substring to replace: ')
replace_with = input('Type in substring to replace with: ')
print(find_replace(phrase, replace_substring, replace_with))





