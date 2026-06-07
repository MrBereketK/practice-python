
# P Y T H O N

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# # n u m p y


# print(np.__version__)

# np_array = np.array([student['score'] for student in students])

# average_numpy = np.mean(np_array)
# print(f"Average of numpy array: {average_numpy}")

# max_numpy = np.max(np_array)
# print(f"Max of numpy array: {max_numpy}")

# min_numpy = np.min(np_array)
# print(f"Min of numpy array: {min_numpy}")


# P A N D A S


# df = pd.DataFrame(students)
# # print(df)

# dfCsv = pd.read_csv('./orders.csv')
# # print(dfCsv)

# # df.head()        # First 5 rows
# # df.tail()        # Last 5 rows
# # df.info()        # Column types and non-null values
# # df.describe()    # Summary stats
# # df.columns      # Column names
# # df.index         # Row indices

# average_score = df["score"].mean()
# max_score = df["score"].max()
# min_score = df["score"].min()

# print("Average:", average_score)
# print("Maximum:", max_score)
# print("Minimum:", min_score)

# print(df["score"].describe())


# M a t p l o t l i p

# # plotting example with matplotlib

# scores = [70, 80, 75, 90, 85]

# plt.plot(scores)
# plt.title("Student Scores")
# plt.xlabel("Student Index")
# plt.ylabel("Score")
# plt.show()

# # bars example with matplotlib
# students = ["John", "Anna", "Mike"]
# scores = [80, 90, 75]

# plt.bar(students, scores)
# plt.show()

# students = ["A", "B", "C"]
# scores = [78, 90, 85]

# plt.bar(students, scores)
# plt.title("Student Scores")
# plt.show()

# # histogram example with matplotlib
# ages = [18, 19, 20, 20, 21, 22, 22, 22, 23, 24]

# plt.hist(ages)
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Count")
# plt.show()