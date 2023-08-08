birthday_is_today = False
number_of_items = 4
price = 10.00

if birthday_is_today and number_of_items > 5:
    price = price * 0.85 * 0.9
elif birthday_is_today:
    price = price * 0.85
elif number_of_items > 5:
    price = price * 0.9

print(price)