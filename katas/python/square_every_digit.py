# Kata Square Every Digit IRL:https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):    
    digit_num = list(str(num))
    solution = ""
    for i in digit_num:
        number = int(i)
        number = number**2
        solution += str(number)
    return print(int(solution))

square_digits(9119)
