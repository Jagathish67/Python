import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = "student.csv"  
df = pd.read_csv(filename)

selected_department = input("enter department:") 
cgpa_threshold = 7.5  


filtered_students = df[(df["DEPARTMENT"] == selected_department) & (df["CGPA"] > cgpa_threshold)]

print("\nFiltered Students (Department:", selected_department, ", CGPA >", cgpa_threshold, ")")
print(filtered_students)
plt.figure(figsize=(10, 5))
sns.barplot(x=filtered_students["NAME"], y=filtered_students["CGPA"], palette="coolwarm")
plt.xticks(rotation=45)
plt.xlabel("Student Name")
plt.ylabel("CGPA")
plt.title(f"CGPA of {selected_department} Students (CGPA > {cgpa_threshold})")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df[df["DEPARTMENT"] == selected_department]["CGPA"], bins=10, kde=True, color="green")
plt.xlabel("CGPA")
plt.ylabel("Frequency")
plt.title(f"CGPA Distribution in {selected_department}")
plt.show()

filtered_students.to_csv("filtered_students.csv", index=False)
print("\nFiltered data saved to 'filtered_students.csv'")

department_counts = df['DEPARTMENT'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%', colors=sns.color_palette('Set3', len(department_counts)), startangle=90)
plt.title('Student Distribution by Department')
plt.show()


avg_cgpa_by_dep = df.groupby('DEPARTMENT')['CGPA'].mean().sort_values()
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_cgpa_by_dep.index, y=avg_cgpa_by_dep.values, palette='Set2')
plt.title('Average CGPA by Department')
plt.xlabel('Department')
plt.ylabel('Average CGPA')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(10, 6))
sns.histplot(df['CGPA'], bins=15, kde=True, color='lightgreen')
plt.title('CGPA Distribution')
plt.xlabel('CGPA')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='YEAR', y='CGPA', hue='DEPARTMENT', palette='Set1', s=100)
plt.title('CGPA vs Year of Study')
plt.xlabel('Year of Study')
plt.ylabel('CGPA')
plt.show()
