students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 90},
    {"name": "Charlie", "grade": 80}
]

students_b = [
    {"name": "David", "grade": 88},
    {"name": "Eve", "grade": 92},
    {"name": "Frank", "grade": 75}
]


sorted_students = sorted(students, key=lambda x: x["grade"])

for x in sorted_students:
    print(x["name"])
