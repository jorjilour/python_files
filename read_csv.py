import csv

filename = "taxables.csv"

def read_csv(filename):
    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(filename, 'r') as csv_file:
        # creating a csv reader object
        csv_reader = csv.reader(csv_file)

        # extracting field names through first row
        fields = next(csv_reader)

        # extracting each data row one by one
        for row in csv_reader:
            rows.append(row)
        n_rows = csv_reader.line_num

    return fields, rows, n_rows


def print_fields(fields):
    # printing the field names
    print("Fields: " + str(fields))
    print('Field names are:' + ', '.join(field for field in fields))


def print_rows(rows):
    #  printing first 5 rows
    # print('\nFirst 5 rows are:\n')
    for row in rows:
        # parsing each column of a row
        row_str = ""
        for col in row:
            row_str += col
        print(row_str)


fields, rows, n_rows = read_csv(filename)
print("Total no. of rows: %d" % n_rows)
print_fields(fields)
print_rows(rows)
