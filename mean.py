import pandas as pd


def calculate_statistics(df, column_name):
    if column_name in df.columns:
        print(f"\nStatistics for column: {column_name}")
        print(f"Mean: {df[column_name].mean():.2f}")
        print(f"Median: {df[column_name].median():.2f}")
        print(f"Standard Deviation: {df[column_name].std():.2f}")
        print(f"Minimum Value: {df[column_name].min()}")
        print(f"Maximum Value: {df[column_name].max()}")
    else:
        print("Invalid column name! Please enter a valid numerical column.")


choice = input("Do you want to enter data manually or upload a CSV file? (manual/csv): ").strip().lower()

if choice == "csv":
    file_path = input("Enter the path of the CSV file: ")
    df = pd.read_csv(file_path)
elif choice == "manual":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    data = {}
    for i in range(cols):
        col_name = input(f"Enter column {i+1} name: ")
        col_values = [float(input(f"Enter value for row {j+1} in {col_name}: ")) for j in range(rows)]
        data[col_name] = col_values

    df = pd.DataFrame(data)
else:
    print("Invalid choice! Exiting program.")
    exit()


print("\nDataset Loaded:\n", df)


print("\nAvailable columns:", list(df.columns))
column_name = input("Enter the column name to analyze: ").strip()


calculate_statistics(df, column_name)