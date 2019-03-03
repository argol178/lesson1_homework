# Задание 1
def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    summ = f"{one}{delimiter}{two}".upper()
    print(summ)
get_summ("Learn","python")

# Задание 2
def format_price(price):
    price = int(price)
    price = f"Цена {price} руб."
    return price
x = format_price(56.24)
print(x)