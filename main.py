import numpy as np
import pandas as pd

# total_score = 0;
# avarage_score = 0

students = [
    {"name": "John", "score": 80},
    {"name": "Sara", "score": 95},
    {"name": "Mike", "score": 70}
]

# for student in students:
#     print(f"Name: {student['name']}, score: {student['score']}")

# for student in students:
#     total_score += student['score'];

# average_score = total_score / len(students);

# print(f"Total score: {total_score}")
# print(f"Average score: {average_score}")

# # using my own algorith to find highest and lowest score
# high = students[0]['score']
# for studnet in students:
#     if student['score'] > high:
#         high = student['score']

#         print(f"Highest score: {high}")

# low = students[0]['score']
# for studnet in students:
#     if student['score'] < low:
#         low = student['score']

#         print(f"Lowest score: {low}")


# # using built-in functions to find highest and lowest score
# highest_score = max(student['score'] for student in students)
# print(f"Highest score: {highest_score}")


# lowest_score = min(student['score'] for student in students)
# print(f"Lowest score: {lowest_score}")

# # practicing with numpy
# print(np.__version__)

# np_array = np.array([student['score'] for student in students])

# average_numpy = np.mean(np_array)
# print(f"Average of numpy array: {average_numpy}")

# max_numpy = np.max(np_array)
# print(f"Max of numpy array: {max_numpy}")

# min_numpy = np.min(np_array)
# print(f"Min of numpy array: {min_numpy}")

df = pd.DataFrame(students)
# print(df)

dfCsv = pd.read_csv('./orders.csv')
# print(dfCsv)

# df.head()        # First 5 rows
# df.tail()        # Last 5 rows
# df.info()        # Column types and non-null values
# df.describe()    # Summary stats
# df.columns      # Column names
# df.index         # Row indices

average_score = df["score"].mean()
max_score = df["score"].max()
min_score = df["score"].min()

print("Average:", average_score)
print("Maximum:", max_score)
print("Minimum:", min_score)

print(df["score"].describe())