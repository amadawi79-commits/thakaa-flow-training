# Task 2: بطاقتك في ذكاء فلو

# 1. المتغيرات
name = "مضاوي شيخ"
city = "Riyadh"
major = "دبلوم ذكاء اصطناعي"
age = 39
coded_before = False
study_hours = 2.5

# 2. طباعة البطاقة بالدمج (+)
print("=== " + name + " ===")
print("City: " + city)
print("Major: " + major)
print("Age: " + str(age))
print("Coded before: " + str(coded_before))
print("Study hours: " + str(study_hours))

print()  # سطر فاضي

# 3. طباعة البطاقة بـ f-string في أمر print واحد فقط
print(f"=== {name} ===\nCity: {city}\nMajor: {major}\nAge: {age}\nCoded before: {coded_before}\nStudy hours: {study_hours}")

# 4. طباعة نوع كل متغير
print("\nأنواع المتغيرات:")
print("name:", type(name))
print("city:", type(city))
print("major:", type(major))
print("age:", type(age))
print("coded_before:", type(coded_before))
print("study_hours:", type(study_hours))

# 5. تعليق: أي طريقة أسهل؟
# f-string أسهل في القراءة وأقصر، وما يحتاج أستخدم str() يدوياً لتحويل الأرقام.
