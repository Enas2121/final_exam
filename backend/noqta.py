
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
