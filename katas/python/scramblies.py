# Kata Multiplication table for number IRL:https://www.codewars.com/kata/55c04b4cc56a697bb0000048

def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True