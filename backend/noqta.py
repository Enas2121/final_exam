
TAX = 0.15


Services = [
    ["WEB", 500],
    ["APP", 2000],
    ["SYSTEM", 7000],
    ["Applied AI", 800],
    ["API", 950]
]

print("Services:")


for i in range(len(Services)):
    print(i + 1, "-", Services[i][0])


num = input("Enter product number: ")

       #دالة تاكد انه ارقام
if num.isdigit():
    num = int(num)

   
    if num >= 1 and num <= len(Services):
        Services = Services[num - 1]   
        name = Services[0]
        price = Services[1]

        total = price + (price * TAX)

        print("Services:", name)
        print("price before tax:", price)
        print("price after tax:", round(total, 2))

    else:
        print("Number out of range. Try again.")
else:
    print("Please enter a number only.")
