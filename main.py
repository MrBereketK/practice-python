total_score = 0;
avarage_score = 0

students = [
    {"name": "John", "score": 80},
    {"name": "Sara", "score": 95},
    {"name": "Mike", "score": 70}
]

for student in students:
    print(f"Name: {student['name']}, score: {student['score']}")

for student in students:
    total_score += student['score'];

average_score = total_score / len(students);

print(f"Total score: {total_score}")
print(f"Average score: {average_score}")


