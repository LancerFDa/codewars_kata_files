# Kata Permute a Palindrome table for number IRL:https://www.codewars.com/kata/58ae6ae22c3aaafc58000079/train/python/


def permute_a_palindrome(input):
    lista_impar = []
    if len(input) == 1:
        return True
    elif len(input) == 2 and input[0] == input[1]:
        return True
    for i in input:
        if input.count(i) % 2 == 1:
            lista_impar += i
    if len(lista_impar) > 1:
        if lista_impar[0] != lista_impar[1]:
            return False
        else:
            return True
    else:
        return True

permute_a_palindrome("baa")
permute_a_palindrome("baabcd")
permute_a_palindrome("aaa")