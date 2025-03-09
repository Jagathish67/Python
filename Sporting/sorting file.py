import csv

def bubble_sort(data, column_index, is_alphabetical=True):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if is_alphabetical:
                if data[j][column_index] > data[j+1][column_index]:
                    data[j], data[j+1] = data[j+1], data[j]
            else:
                if int(data[j][column_index]) > int(data[j+1][column_index]):
                    data[j], data[j+1] = data[j+1], data[j]
    return data

def read_csv(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        return list(reader)

def write_csv(file_name, data):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
def sort_csv(input_file, output_file, column_index, is_alphabetical=True):
    data = read_csv(input_file)
    headers = data[0] 
    data = data[1:]  
    sorted_data = bubble_sort(data, column_index, is_alphabetical)
    sorted_data.insert(0, headers) 
    write_csv(output_file, sorted_data)


input_file = 'unordersort.csv'  
output_file = 'sorted.csv' 
column_index = 0 
is_alphabetical = False 

sort_csv(input_file, output_file, column_index, is_alphabetical)
