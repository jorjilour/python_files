import pandas as pd

import matplotlib.pyplot as plt

csv_file = 'taxables.csv'
data = pd.read_csv(csv_file)

Item, Cost = [], []
print(data.head(7))
print(data.describe())
print(data.info())

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

Item = data['Item']
Cost = data['Cost']


x=list(Item)
y=list(Cost)

print('x ' + str(len(x)))
print(len(y))


plt.bar(x, y)
plt.xlabel('Item->')
plt.ylabel('Cost->')
plt.title('Data')
plt.show()
