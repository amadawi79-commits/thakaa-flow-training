# Task 4: رسالة تأكيد حجز آلية

# 1. استقبال البيانات
customer = input("Customer name: ")
service = input("Service: ")
date = input("Date (YYYY-MM-DD): ")
time = input("Time (HH:MM): ")
price = float(input("Service price: "))
booking_no = int(input("Booking number: "))
session_minutes = int(input("Session length (minutes): "))

# 2. الحسابات
deposit = price * 0.30
remaining = price - deposit
hours = session_minutes // 60
minutes = session_minutes % 60
booking_code = f"TF-2026-{booking_no:04d}"

# 3. طباعة رسالة التأكيد
print(f"\nHello {customer},")
print(f'Your booking for "{service}" is confirmed.')
print(f"Date: {date} at {time}")
print(f"Session Length: {hours} h {minutes} min")
print(f"Booking code: {booking_code}")
print(f"Deposit due: {deposit:.2f} SAR")
print(f"Remaining on delivery: {remaining:.2f} SAR")
print("Thank you for choosing Thakaa Flow!")
