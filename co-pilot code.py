#Ctrl + Enter to see a pane full of suggestions. 

# get cryptocurrency price data from coinmarketcap.com
# import requests
# import json

# def get_cryptocurrency_data():
#     url = 'https://api.coinmarketcap.com/v1/ticker/?limit=10'
#     response = requests.get(url)
#     return response.json()

# def get_cryptocurrency_price(cryptocurrency):
#     for currency in get_cryptocurrency_data():
#         if currency['symbol'] == cryptocurrency:
#             return currency['price_usd']

# print(get_cryptocurrency_price('BTC'))

## get data from online 

# get weather for a city with weatherbit
# def get_weather(city):
#     ''' Get weather for a city '''
#     import requests
#     url = 'https://api.weatherbit.io/v2.0/current?city=' + city + '&key=acb1414a0398431495b6cbbbbbce6294'
#     r = requests.get(url)
#     data = r.json()
#     return data['data'][0]['temp']

# print(get_weather('Miami'))


#check if email is valid 
# def is_valid_email(email):
#     ''' Check if email is valid '''
#     import re
#     if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
#         return True
#     return False

# print (is_valid_email('zgui@gmail.com'))

#solving for leetcode quesitons
# a program that converts a roman numeral to an integer
# ROMAN_NUMERAL = {
#     "I":1,
#     "V":5,
#     "X":10,
#     "L":50,
#     "C":100,
#     "D":500,
#     "M":1000
# }
# def roman_to_int(roman_numeral: str) -> int:
#     total = 0
#     for i in range(len(roman_numeral)):
#         if i > 0 and ROMAN_NUMERAL[roman_numeral[i]] > ROMAN_NUMERAL[roman_numeral[i-1]]:
#             total += ROMAN_NUMERAL[roman_numeral[i]] - 2 * ROMAN_NUMERAL[roman_numeral[i-1]]
#         else:
#             total += ROMAN_NUMERAL[roman_numeral[i]]
#     return total

# Test_Cases = [
#     ("III", 3),
#     ("IV", 4),
#     ("IX", 9),
#     ("LVIII", 58),
# ]
# for test_input, expected in Test_Cases:
#     # assert roman_to_int(test_input) == expected
#     # print("Test passed for input: ", test_input)
#     total = roman_to_int(test_input)
#     print(total, total == expected)
# useful and cut timie for coding because makes you worse at coding. skill will decay.  
# it will shift your skills into different kind of coding. like problem solving at more stragetic level. 
#focusing on design and business application of your software. 
# concern? privacy, security, and data.

#give me an program that check for odd number
def is_odd(number):
    if number % 2 == 0:
        return False
    return True