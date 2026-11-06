# Kata Duplicate Encode IRL:https://www.codewars.com/kata/5571f712ddf00b54420000ee/train/python


def loose_change(cents):

    coin_key=["Nickles", "Pennies", "Dimes", "Quarters"]
    coin_values = [5, 1, 10, 25]

    wallet = dict(zip(coin_key, coin_values)) 

    coins = list(sorted(wallet.values()))

    change = []
    coins_available = len(coins) -1
    while cents > 0 and coins_available >= 0:
        if cents >= coins[coins_available]:
            cents -= coins[coins_available]
            change.append(coins[coins_available])
        else:
            coins_available -= 1

    change_dict = dict.fromkeys(coin_key, 0)
    for coin in change:
        for coin_name in wallet:
            if wallet[coin_name] == coin:
                change_dict[coin_name] += 1

    return change_dict

    

assert loose_change(29),  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
assert loose_change(91),  {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
assert loose_change(0),   {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
# assert loose_change(-2),  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
assert loose_change(3.9), {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}