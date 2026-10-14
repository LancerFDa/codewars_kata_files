# Kata Conver_to_camel_case IRL:https://www.codewars.com/kata/517abf86da9663f1d2000003/solutions/python

def to_camel_case(input):
    result = ""
    next_upper = False
    for i in input:
        if i == "_" or i == "-":
            next_upper = True
        elif next_upper == True:
            result += i.upper()
            next_upper = False
        else:
            result += i
    return result


to_camel_case("the-stealth-warrior")