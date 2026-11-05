def to_minutes(time_text):
    hours, minutes = time_text.split(":")
    return int(hours) * 60 + int(minutes)


def daily_points(checkin, on_time, total_tasks, report_on_time, scores):
    attendance = 5 if to_minutes(checkin) < to_minutes("10:00") else 0
    report = 5 if report_on_time else 0

    tasks = 0
    quality = 0
    if total_tasks > 0:
        tasks = 10 * (on_time / total_tasks)
        quality = 10 * (sum(scores) / (10 * total_tasks))

    return attendance + tasks + report + quality


trainees = [
    {"name": "Sara", "checkin": "09:40", "on_time": 5,
     "report_on_time": False, "scores": [8, 8, 8, 8, 8]},
    {"name": "Omar", "checkin": "10:15", "on_time": 4,
     "report_on_time": True, "scores": [9, 9, 9, 9, 9]},
    {"name": "Lina", "checkin": "08:55", "on_time": 5,
     "report_on_time": True, "scores": [10, 9, 9, 10, 8]},
    {"name": "Madawi", "checkin": "09:00", "on_time": 5,
     "report_on_time": True, "scores": [10, 10, 10, 9, 9]}
]

# نقاط مضاوي: 5 حضور + 10 مهام + 5 تقرير + 9.6 جودة = 29.6
# نقاط Lina هي 29.2، لذلك الفرق الحسابي 0.4 نقطة.
total_tasks = 5
total_points = 0
best = None

for trainee in trainees:
    trainee["points"] = daily_points(
        trainee["checkin"], trainee["on_time"], total_tasks,
        trainee["report_on_time"], trainee["scores"]
    )
    total_points += trainee["points"]
    print(f'{trainee["name"]}: {trainee["points"]:.1f}')

    if best is None or trainee["points"] > best["points"]:
        best = trainee

print(f"Average: {total_points / len(trainees):.1f}")
print(f'Best of the Day: {best["name"]}')

# تمثيل الكسور العشرية قد يجعل الفرق الخام قريبًا من 0.4.
# تنسيق الطباعة إلى منزلة واحدة يعرضه بالشكل المتوقع.
difference = trainees[3]["points"] - trainees[2]["points"]
print("Raw difference:", difference)
print(f"Formatted difference: {difference:.1f}")

# اختبار يوم بلا مهام: نقاط المهام والجودة صفر، والناتج 10.
print("No tasks:", daily_points("09:00", 0, 0, True, []))
