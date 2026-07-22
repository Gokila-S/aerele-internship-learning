def calculate_discount(price):
    return price * 0.9


price = input("Enter price: ")

try:
    price = float(price)

    if price < 0:
        raise ValueError("Price cannot be negative.")

    print(calculate_discount(price))

except ValueError as e:
    print(e)
