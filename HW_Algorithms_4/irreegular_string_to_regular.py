
def normalize_string(string):
    string = string.lower().split()
    string = ' '.join(string)
    string = string[0].upper() + string[1:]
    return string


irregular_phrase = " NoNe oF   us WiLl evEr meet THE snow man   "

# print(normalize_string(irregular_phrase))
