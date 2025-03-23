import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("student.csv")


summary = df.groupby("Department").agg(
    Total_Students=("Student_ID", "count"),
    Pass_Count=("Pass/Fail", lambda x: (x == "Pass").sum()),
    Fail_Count=("Pass/Fail", lambda x: (x == "Fail").sum()),
    Pass_Percentage=("Pass/Fail", lambda x: (x == "Pass").mean() * 100),
    Average_CGPA=("CGPA", "mean")
).reset_index()

print("\nOverall Department-Wise Summary:")
print(summary)


plt.figure(figsize=(8, 5))
summary.plot(x="Department", y=["Pass_Count", "Fail_Count"], kind="bar", stacked=True, colormap="viridis", figsize=(8,5))
plt.title("Pass vs Fail Count Per Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.xticks(rotation=45)
plt.legend(["Pass", "Fail"])
plt.show()


plt.figure(figsize=(6, 6))
plt.pie(summary["Pass_Percentage"], labels=summary["Department"], autopct="%1.1f%%", colors=["#4CAF50", "#FFC107", "#FF5722", "#03A9F4", "#9C27B0"])
plt.title("Pass Percentage by Department")
plt.show()


plt.figure(figsize=(8, 5))
sns.boxplot(x="Department", y="CGPA", data=df, palette="Set2")
plt.title("CGPA Distribution by Department")
plt.xlabel("Department")
plt.ylabel("CGPA")
plt.xticks(rotation=45)
plt.show()