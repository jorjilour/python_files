from read_csv import read_csv as read_file
import pandas as pd

filename = 'taxables.csv'
write_file = 'result.csv'

fields, rows, n_rows = read_file(filename)

df = pd.read_csv(filename)

#find out who has the highest total
max_total = df['Total'].max()
print(max_total)
print(df['Total'].value_counts())

