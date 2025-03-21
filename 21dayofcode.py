import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("student.csv")


print("Summary Statistics:")
print(data.describe())


correlation = data['Exam_Score'].corr(data['Attendance'])
print(f"\nCorrelation between Exam Score and Attendance: {correlation:.2f}")


plt.figure(figsize=(8, 5))
sns.histplot(data['Exam_Score'], bins=10, kde=True, color='blue')
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x=data['Attendance'], y=data['Exam_Score'], color='red')
plt.title("Exam Score vs Attendance")
plt.xlabel("Attendance (%)")
plt.ylabel("Exam Score")
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(y=data['Exam_Score'], color='green')
plt.title("Exam Score Box Plot")
plt.ylabel("Exam Score")
plt.show()

top_students = data.sort_values(by="Exam_Score", ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_students["Student"], y=top_students["Exam_Score"], palette="viridis")
plt.xticks(rotation=45)
plt.title("Top 10 Students by Exam Score")
plt.xlabel("Student")
plt.ylabel("Exam Score")
plt.show()