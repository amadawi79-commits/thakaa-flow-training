# Task 3: فاتورة متجر إلكتروني

# 1. استقبال البيانات
customer = input("Customer name: ")
product = input("Product: ")
unit_price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

# 2. الحسابات
subtotal = unit_price * quantity
discount = subtotal * 0.10
after_discount = subtotal - discount
vat = after_discount * 0.15
total = after_discount + vat

# 3. طباعة الفاتورة
print("\n========== INVOICE ==========")
print(f"Customer: {customer}")
print(f"Product: {product} x {quantity}")
print(f"Subtotal: {subtotal:.2f} SAR")
print(f"Discount (10%): {discount:.2f} SAR")
print(f"After discount: {after_discount:.2f} SAR")
print(f"VAT (15%): {vat:.2f} SAR")
print(f"Total: {total:.2f} SAR")
