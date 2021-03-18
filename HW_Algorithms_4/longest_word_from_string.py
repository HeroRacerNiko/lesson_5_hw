
def longest_word(string):
    string = string.split()
    longest = string[0]
    for word in string:
        if len(word) > len(longest):
            longest = word
    return longest


phrase = 'Every person has good days and bad days. The anticipation of better days is crucial'
# print(longest_word(phrase))
