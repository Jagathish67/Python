import csv

def load_sorted_csv(filename):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        
        if not data:
            print("The file is empty. Please provide a valid dataset.")
            return None
        
        return sorted(data, key=lambda x: int(x["ID"]))
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
        return None
    except Exception as e:
        print(f" Error reading file: {e}")
        return None

def binary_search(data, search_id):

    low, high = 0, len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_id = int(data[mid]["ID"])

        if mid_id == search_id:
            return data[mid] 
        elif mid_id < search_id:
            low = mid + 1 
        else:
            high = mid - 1  

    return None 

filename = input("Enter the CSV filename (with extension, e.g., students.csv): ").strip()

data = load_sorted_csv(filename)

if data:
    while True:
        search_id = input("\n Enter Student ID to search (or type 'exit' to quit): ")
        
        if search_id.lower() == "exit":
            print(" Exiting program. Goodbye!")
            break

        if not search_id.isdigit():
            print("Please enter a valid numeric ID.")
            continue

        search_id = int(search_id)
        result = binary_search(data, search_id)

        if result:
            print("\ Record Found:")
            for key, value in result.items():
                print(f"{key}: {value}")
        else:
            print("No record found.")