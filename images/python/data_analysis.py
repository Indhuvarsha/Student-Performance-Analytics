import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("../dataset/student_performance.csv")

# Display the first five records
print("First Five Records:")
print(data.head())

# Display basic information
print("\nDataset Information:")
print(data.info())

# Calculate averages
print("\nAverage Values:")
print(data[["Attendance", "Study_Hours", "Assignment", "Internal", "Final_Mark"]].mean())

# Find the highest performing student
highest_student = data.loc[data["Final_Mark"].idxmax()]
print("\nHighest Performing Student:")
print(highest_student)

# Find the lowest performing student
lowest_student = data.loc[data["Final_Mark"].idxmin()]
print("\nLowest Performing Student:")
print(lowest_student)

# Attendance vs Final Marks
plt.figure(figsize=(8, 5))
plt.scatter(data["Attendance"], data["Final_Mark"])
plt.xlabel("Attendance")
plt.ylabel("Final Mark")
plt.title("Attendance vs Final Mark")
plt.grid(True)
plt.savefig("attendance_vs_marks.png")
plt.show()

# Study Hours vs Final Marks
plt.figure(figsize=(8, 5))
plt.scatter(data["Study_Hours"], data["Final_Mark"])
plt.xlabel("Study Hours")
plt.ylabel("Final Mark")
plt.title("Study Hours vs Final Mark")
plt.grid(True)
plt.savefig("study_hours_vs_marks.png")
plt.show()

# Student vs Final Marks
plt.figure(figsize=(10, 5))
plt.bar(data["Student"], data["Final_Mark"])
plt.xlabel("Student")
plt.ylabel("Final Mark")
plt.title("Student Final Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("student_final_marks.png")
plt.show()

print("\nAnalysis completed successfully!")