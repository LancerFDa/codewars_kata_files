# Kata Multiplication table for number IRL:https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/python

def multiTable(n):

    tabla = ""
    for i in range(1, 11):
        if i == 10:
            tabla += f"{i} * {n} = {i * n}"
        else:
            tabla += f"{i} * {n} = {i * n} \n"
    return tabla

multiTable(5)