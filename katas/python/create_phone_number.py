# Kata Create Phone Number IRL:https://www.codewars.com/kata/525f50e3b73515a6db000b83/solutions/python

def create_phone_number(n):
    phone_number = ""
    first_digits = ""
    second_digits = ""
    third_digits = ""
    for i in n[0:3]:
        first_digits += str(i)
    for i in n[3:6]:
        second_digits += str(i)
    for i in n[6:]:
        third_digits += str(i)
    phone_number += f"({first_digits}) {second_digits}-{third_digits}"
    return phone_number
        
create_phone_number([2, 2, 3, 4, 5, 6, 7, 8, 9, 0])