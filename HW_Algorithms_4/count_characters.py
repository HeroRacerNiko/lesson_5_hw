from longest_word_from_string import phrase


def count_characters(string, substring):
    result = {substring: 0}
    string = string.lower()
    if len(substring) == 1:
        for char in string:
            if char not in result:
                result[char] = 0
            else:
                result[char] += 1
        return result[substring]
    else:
        while substring in string:
            result[substring] += 1
            string = string[string.index(substring) + len(substring)::]
        return result[substring]


print(count_characters(phrase, 'ay'))
