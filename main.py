total_score = 0;
avarage_score = 0

students = [
    {"name": "John", "score": 80},
    {"name": "Sara", "score": 95},
    {"name": "Mike", "score": 70}
]

for student in students:
    print(f"Name: {student['name']}, score: {student['score']}")

# for student in students:
#     total_score += student['score'];

# average_score = total_score / len(students);

# print(f"Total score: {total_score}")
# print(f"Average score: {average_score}")

# using my own algorith to find highest and lowest score
high = students[0]['score']
for studnet in students:
    if student['score'] > high:
        high = student['score']

        print(f"Highest score: {high}")

low = students[0]['score']
for studnet in students:
    if student['score'] < low:
        low = student['score']

        print(f"Lowest score: {low}")


# using built-in functions to find highest and lowest score
highest_score = max(student['score'] for student in students)
print(f"Highest score: {highest_score}")


lowest_score = min(student['score'] for student in students)
print(f"Lowest score: {lowest_score}")