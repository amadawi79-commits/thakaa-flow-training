days = ["Sun", "Mon", "Tue", "Wed", "Thu"]
sales = [1200, 950, 1800, 1430, 2100]

total = 0
best_index = 0
above_target = 0

# نستخدم الفهرس لربط مبيعات كل يوم باسمه في قائمة days.
# أما for s in sales فتعطينا قيمة المبيعات وحدها.
for i in range(len(sales)):
    print(f"{days[i]}: {sales[i]} SAR")

    total += sales[i]

    if sales[i] > sales[best_index]:
        best_index = i

    if sales[i] > 1500:
        above_target += 1

    average = total / (i + 1)

print(f"Total: {total} SAR")
print(f"Average: {average:.0f} SAR")
print(f"Best day: {days[best_index]} ({sales[best_index]} SAR)")
print(f"Days above target: {above_target}")
