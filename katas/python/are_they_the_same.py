def comp(number_list_a,number_list_b):

    if number_list_a is None or number_list_b is None:
        return False
    if len(number_list_a) != len(number_list_b):
        return False

    number_list_a.sort()
    number_list_b.sort()

    counter = 0
    for i in number_list_a:
        if i**2 != number_list_b[counter]:
            return False
        counter += 1
    return True

if "__main__"==__name__:

        a1 = [121, 144, 19, 161, 19, 144, 19, 11] 
        a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

        comp(a1, a2) is True

        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

        comp(a1, a2) is False