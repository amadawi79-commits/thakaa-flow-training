def add_vat(amount, rate=0.15):
    if not isinstance(amount, (int, float)) or amount < 0:
        return "Invalid amount"
    return round(amount * (1 + rate), 2)


def format_price(amount):
    if not isinstance(amount, (int, float)) or amount < 0:
        return "Invalid amount"
    return f"{amount:,.2f} SAR"


def is_valid_phone(phone):
    if not isinstance(phone, str):
        return False
    return (
        len(phone) == 10
        and phone.isascii()
        and phone.isdigit()
        and phone.startswith("05")
    )


# اختبار كل دالة بثلاث قيم، منها قيمة خاطئة.
print(add_vat(1000))
print(add_vat(200))
print(add_vat(-50))

print(format_price(1234.5))
print(format_price(0))
print(format_price("abc"))

print(is_valid_phone("0551234567"))
print(is_valid_phone("0661234567"))
print(is_valid_phone("05512"))

# استخدام الدالتين معًا.
print(format_price(add_vat(1000)))

# طباعة الأرقام الصحيحة وعددها.
phones = [
    "0551234567",
    "0661234567",
    "055 123 4567",
    "05512",
    "05abc12345"
]

valid_count = 0
for phone in phones:
    if is_valid_phone(phone):
        print(phone)
        valid_count += 1

print("Valid phones:", valid_count)
