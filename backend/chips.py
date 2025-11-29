TAX = 0.15

# المنتجات (الاسم، السعر قبل الضريبة)
Chips = [
   ("doritos" , 9),
   ("lays" , 7),
   ("pringles" , 12),
   ("cheetos" , 8),
   ("takis" , 5),
]
# 1) عرض المنتجات مع أرقامها
print("المنتجات المتاحة:")
for i, (name, price) in enumerate(Chips, start=1):
    print(i, "-", name)

# 2) طلب رقم المنتج
num = input("Enter number product ").strip()

# 3) محاولة تحويل الإدخال إلى رقم صحيح
if not num.isdigit():
    print("Enter number")
else:
    idx = int(num)  # رقم المنتج
    # 4) التحقق إذا كان الرقم داخل النطاق
    if 1 <= idx <= len(Chips):
        name, base_price = Chips[idx - 1]
        total = base_price * (1 + TAX)  # السعر بعد الضريبة
        # 5) عرض النتيجة
        print(f"product: {name}")
        print(f"prise pefor tax: {base_price:.2f}")
        print(f"prise after tax: {total:.2f}")
    else:
        print("الرقم خارج النطاق. جرب رقم بين 1 و", len(Chips))