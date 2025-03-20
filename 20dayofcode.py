import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("student.csv")

study_hours = data["Study_Hours"][0]
attendance = data["Attendance"][0]
subjects = ["ML", "FDS", "CN", "ESS", "PAS", "OS"]
marks = data.iloc[0, 2:].values  


plt.figure(figsize=(10, 5))
sns.barplot(x=subjects, y=marks, palette="viridis")
plt.title("Marks in Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.show()

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie([study_hours, 10 - study_hours], labels=["Study Hours", "Remaining"],
       autopct='%1.1f%%', colors=['skyblue', 'lightgray'], startangle=90)
plt.title("Daily Study Hours")

plt.figure(figsize=(6, 6))
plt.pie([attendance, 100 - attendance], labels=["Attendance", "Absent"],
        autopct='%1.1f%%', colors=['green', 'red'], startangle=90)
plt.title("Attendance Percentage")

plt.show()