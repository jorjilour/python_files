import pandas as pd

import matplotlib.pyplot as plt

csv_file = 'taxable2.csv'
data = pd.read_csv(csv_file)

Item, Cost = [], []

print(data)
Item = data['Item']
Cost = data['Cost']


x=list(Item)
y=list(Cost)

print('x ' + str(len(x)))
print(len(y))


plt.pie(y,labels=x, autopct='%.2f%%')
plt.ylabel('Cost->')
plt.title('Data')
plt.show()
