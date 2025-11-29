"""TAX = 0.15

Services = [
    ("doritos" , 9),
    ("lays" , 7),
    ("pringles" , 12),
    ("cheetos" , 8),
    ("takis" , 5),
]

print("products:")
for i, (name, price) in enumerate(Services, start=1):
    print(i, "-", name)

num = input("Enter product number ").strip()

if not num.isdigit():
    print("Enter number")
else:
    idx = int(num)
    if 1 <= idx <= len(Services):
        name, base_price = Services[idx - 1]
        total = base_price * (1 + TAX)
        print(f"product: {name}")
        print(f"price before tax: {base_price:.2f}")
        print(f"price after tax: {total:.2f}")
    else:
        print("Number out of range. Try a number between 1 and", len(Services))"""

 
TAX = 0.15


Services = [
    ["WEB", 500],
    ["APP", 2000],
    ["SYSTEM", 7000],
    ["Applied AI", 800],
    ["API", 950]
]

print("products:")


for i in range(len(Services)):
    print(i + 1, "-", Services[i][0])


num = input("Enter product number: ")


if num.isdigit():
    num = int(num)

   
    if num >= 1 and num <= len(Services):
        product = Services[num - 1]   
        name = product[0]
        price = product[1]

        total = price + (price * TAX)

        print("product:", name)
        print("price before tax:", price)
        print("price after tax:", round(total, 2))

    else:
        print("Number out of range. Try again.")
else:
    print("Please enter a number only.")
