# Kata Duplicate Encode IRL:https://www.codewars.com/kata/525f50e3b73515a6db000b83/solutions/python

def duplicate_encode(word):
    lower_word = word.lower()
    result = ""
    for i in lower_word:
        if lower_word.count(i) == 1:
            result += "("
        else:
            result += ")"
    return result



duplicate_encode("Success")
duplicate_encode("caca")