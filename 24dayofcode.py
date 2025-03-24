import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("dataset.csv", parse_dates=["Admission_Date", "Discharge_Date"])


df["Length_of_Stay"] = (df["Discharge_Date"] - df["Admission_Date"]).dt.days
df.dropna(inplace=True)  


print("Summary Statistics:\n", df.describe())

# Age Distribution of Patients
plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=10, kde=True, color="skyblue")
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Gender Distribution
plt.figure(figsize=(6, 5))
df["Gender"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["lightblue", "pink"])
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# Most Common Diagnoses
plt.figure(figsize=(8, 5))
sns.countplot(y=df["Diagnosis"], order=df["Diagnosis"].value_counts().index, palette="coolwarm")
plt.title("Top Diagnoses")
plt.xlabel("Count")
plt.ylabel("Diagnosis")
plt.show()

# Treatment Cost by Department
plt.figure(figsize=(10, 5))
sns.barplot(x="Department", y="Treatment_Cost", data=df, ci=None, palette="viridis")
plt.title("Average Treatment Cost by Department")
plt.xticks(rotation=45)
plt.show()

#  Insurance Coverage Distribution
plt.figure(figsize=(6, 10))
df["Insurance_Covered"].value_counts().plot(kind="bar", color=["green", "red"])
plt.title("Insurance Coverage")
plt.xlabel("Covered by Insurance")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()

#  Hospital Admissions Over Time
plt.figure(figsize=(10, 5))
df["Admission_Date"].groupby(df["Admission_Date"].dt.month).count().plot(kind="line", marker="o", color="purple")
plt.title("Hospital Admissions Trend")
plt.xlabel("Month")
plt.ylabel("Number of Admissions")
plt.show()

#  Length of Stay Distribution
plt.figure(figsize=(8, 5))
sns.boxplot(x="Department", y="Length_of_Stay", data=df, palette="Set2")
plt.title("Length of Stay by Department")
plt.xticks(rotation=45)
plt.show()

#  Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# Save Cleaned Data
df.to_csv("cleaned_hospital_data.csv", index=False)
print("Cleaned dataset saved as 'cleaned_hospital_data.csv'")