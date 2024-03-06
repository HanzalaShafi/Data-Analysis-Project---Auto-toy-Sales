import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('AutoSalesdata.csv')


# Convert ORDERDATE to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Sales trends over time // orsa = orderdate and sales
orsa = df.groupby(df['ORDERDATE'].dt.to_period("M"))['SALES'].sum()
orsa.plot(
    kind='line', 
    title='Monthly Sales Trend')
plt.show()

# Sales by product line // prsa = productline and sales
prsa = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
ax = prsa.plot(
    kind='bar', 
    title='Sales by Product Line')

for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, str(int(i.get_height())), ha='center', va='bottom')

plt.show()

coqu = df.groupby('COUNTRY')['QUANTITYORDERED'].sum()
coqu.plot(
    kind='pie',
    title='Quantity ordered by Country',
    autopct='%1.1f%%',
    textprops={'fontsize': 6.5})
plt.ylabel('')  # This removes the 'QUANTITYORDERED' label on the y-axis
plt.show()

prqu = df.groupby('PRODUCTLINE')['QUANTITYORDERED'].sum().sort_values(ascending=False)
ax2 = prqu.plot(
    kind='bar',
    title = 'Quantity ordered by Product Line')
for i in ax2.patches:
    ax2.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, str(int(i.get_height())), ha='center', va='bottom')
plt.show()

stqu = df.groupby('STATUS')['QUANTITYORDERED'].sum().sort_values(ascending=False)
ax3 = stqu.plot(
    kind='bar',
    title = 'Status of each Quatity Ordered')
for i in ax3.patches:
    ax3.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, str(int(i.get_height())), ha='center', va='bottom')
plt.show()

dequ = df.groupby('DEALSIZE')['QUANTITYORDERED'].sum().sort_values(ascending=False)
dequ.plot(
    kind='bar',
    title = 'Deal Size of the Quantity Ordered')
plt.show()


df['YEAR'] = df['ORDERDATE'].dt.year
yequ = df.groupby('YEAR')['QUANTITYORDERED'].sum().sort_values(ascending=False)
yequ.plot(
    kind='bar',
    title = 'Quantity Ordered by YEAR')
