# Kata Sum of Array Singles for number IRL:https://www.codewars.com/kata/59f11118a5e129e591000134/train/python

def repeats(arr):
    result = []
    for i in arr:
        if arr.count(i) == 1:
            result.append(i)
    return sum(result)

repeats([4,5,7,5,4,8])