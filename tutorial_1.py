products = {
    "101": ("Milk", 2.50),
    "102": ("Eggs", 3.00),
    "103": ("Bread", 1.75),
    "104": ("Cheese", 4.50),
    "105": ("Apple", 0.50)
}

cart = ["101", "105", "105", "999", "103", "105"]
overall_price=0
for item in cart:
    if item in products:
        name, price = products[item]
        print(f"{name}: {price}")
        overall_price+=price
print(20*"-")
print(overall_price)






