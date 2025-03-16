import csv

def search_by_id(filename, search_id):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ID"] == search_id:  
                return row 

    return None 

filename = "Student.csv"

while True:
    search_id = input("\nEnter ID to search (or type 'exit' to stop): ")
    
    if search_id.lower() == "exit":
        print("Exiting program. Goodbye!")
        break 
    
    result = search_by_id(filename, search_id)

    if result:
        print("\nRecord Found:")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print("No record found.")
