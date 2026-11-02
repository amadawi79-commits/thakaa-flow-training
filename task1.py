# Task 1: اقرأ الكود قبل أن تشغله

a = "7"
b = 3
print(type(a), type(b))
# print(a + b)          # هذا السطر يعطي خطأ
print(int(a) + b)
print(a + str(b))
print(int(a) / b)
print(int(a) // b, int(a) % b)

# --- الإجابات ---
# 1. جدول التوقعات موجود في الملف النصي أو الشرح السابق
# 2. المتغير مثل صندوق تخزن فيه قيمة
# 3. الخطأ: TypeError لأن age نص
# الإصلاح بالدمج:
# print("Hello " + name + ", in 5 years you will be " + str(int(age) + 5))
# الإصلاح بـ f-string:
# print(f"Hello {name}, in 5 years you will be {int(age) + 5}")
# 4. input() يرجع نص دائماً
# ValueError: invalid literal for int() with base 10: 'twenty'
