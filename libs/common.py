import csv

def read_csv(filepath=''):
    rows = []
    with open(filepath, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    return rows

def write_csv(data='', filepath=''):
    with open(filepath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in data:
            csvwriter.writerow(row)

def print_array_as_grid(data):
    # Find the maximum length of any element in the data
    max_length = 0
    for row in data:
        for element in row:
            max_length = max(max_length, len(element))
  
    # Add a box around the grid
    column_subsection = '+' + ( '-' * (max_length+2) )
    print(column_subsection * len(data[0]) + '+')
    for row in data:
        print('| ' + ' | '.join(element.ljust(max_length) for element in row) + ' |')
        print(column_subsection * len(data[0]) + '+')

if __name__ == '__main__':
    # print('If you are seeing this, common.py is running as the primary script.')
    rows = read_csv('habit-test.csv')
    print(rows)
    write_csv(rows, 'csv-export-test.csv')

    print_array_as_grid(rows)