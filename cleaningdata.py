import pandas as pd
import matplotlib.pyplot as plt

csv_file = 'temporal.csv'
data = pd.read_csv(csv_file)

# We make sure that the Month column has datetime format
format_dict = {'data science': '${0:,.2f}', 'Mes': '{:%m-%Y}', 'machine learning': '{:.02f%}',
               'deep learning': '{:.02f%}'}
# We apply the style to the visualization
data['Mes'] = pd.to_datetime(data['Mes'])


data.head().style.format(format_dict)
data.head().style.format(format_dict).highlight_max(color='darkgreen').highlight_min(color='#ff0000')

print(data.info())
print(data.describe())


# REPLACING VALUES
# Loop through all values in the "Duration" column.
# If the value is higher than 90, set it to 90:
for x in data.index:
  if data.loc[x, "data science"] > 90:
    data.loc[x, "data science"] = 90

print(data.to_string())

# REMOVING ROWS IF AN OUTLIER
for x in data.index:
  if data.loc[x, "data science"] < 10:
    data.drop(x, inplace=True)

print(data.to_string())

# TEST AND REMOVE DUPLICATES
print(True in data.duplicated())

data.drop_duplicates(inplace = True)

print(data.head(10).to_string())

