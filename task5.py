# Task 5: رسالة إلى المريخ

# 1. استقبال البيانات
distance = float(input("Distance (million km): "))
age_earth = float(input("Your age (Earth years): "))
weight_earth = float(input("Your weight on Earth (kg): "))

# 2. الحسابات
# سرعة الضوء ≈ 299792 كم/ث
speed_of_light = 299792
distance_km = distance * 1_000_000
travel_seconds = distance_km / speed_of_light
travel_minutes = int(travel_seconds // 60)
travel_secs = int(travel_seconds % 60)

round_trip_seconds = travel_seconds * 2
round_hours = int(round_trip_seconds // 3600)
round_minutes = int((round_trip_seconds % 3600) // 60)
round_secs = int(round_trip_seconds % 60)

# سنة المريخ ≈ 687 يوم أرضي، سنة الأرض ≈ 365.25
age_mars = age_earth * (365.25 / 687)

# الجاذبية على المريخ ≈ 38% من الأرض
weight_mars = weight_earth * 0.38

# يوم المريخ (Sol) ≈ 24 ساعة و 39 دقيقة و 35 ثانية
sol_seconds = 24*3600 + 39*60 + 35
earth_week_sols = (7 * 24 * 3600) / sol_seconds

# 3. طباعة التقرير
print("\n=== MARS MISSION REPORT ===")
print(f"Message travel time: {travel_minutes} min {travel_secs} sec")
print(f"Round trip: {round_hours} h {round_minutes} min {round_secs} sec")
print(f"Your age on Mars: {age_mars:.2f} years")
print(f"Your weight on Mars: {weight_mars:.2f} kg")
print(f"One Earth week = {earth_week_sols:.2f} Mars sols")
