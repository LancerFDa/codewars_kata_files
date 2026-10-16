# Kata Permute a Palindrome table for number IRL:https://www.codewars.com/kata/58ae6ae22c3aaafc58000079/train/python/

def permute_a_palindrome(input):
    impares = 0
    for char in set(input):
        contador = input.count(char)
        if contador % 2 != 0:
            impares += 1
    return impares <= 1
                
permute_a_palindrome("aa")
permute_a_palindrome("baa")
permute_a_palindrome("bacb")
