import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path =("C:\\Users\\MY\\Downloads\\Amazon Sales data.csv")
data = pd.read_csv(file_path)

# Convert 'Order Date' to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'])

# Extract year and month
data['Year'] = data['Order Date'].dt.year
data['Month'] = data['Order Date'].dt.month

# Monthly Sales Trend
monthly_sales = data.groupby(['Year', 'Month'])['Total Revenue'].sum().reset_index()

# Plot Monthly Sales Trend
plt.figure(figsize=(12, 6))
for year in monthly_sales['Year'].unique():
    plt.plot(monthly_sales[monthly_sales['Year'] == year]['Month'], 
             monthly_sales[monthly_sales['Year'] == year]['Total Revenue'], 
             label=year)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.legend(title='Year')
plt.show()

# Yearly Sales Trend
yearly_sales = data.groupby('Year')['Total Revenue'].sum().reset_index()

# Plot Yearly Sales Trend
plt.figure(figsize=(12, 6))
plt.plot(yearly_sales['Year'], yearly_sales['Total Revenue'], marker='o')
plt.title('Yearly Sales Trend')
plt.xlabel('Year')
plt.ylabel('Total Revenue')
plt.show()

# Yearly Month-wise Sales Trend
yearly_monthly_sales = data.groupby(['Year', 'Month'])['Total Revenue'].sum().unstack().fillna(0)

# Plot Yearly Month-wise Sales Trend
yearly_monthly_sales.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Yearly Month-wise Sales Trend')
plt.xlabel('Year')
plt.ylabel('Total Revenue')
plt.legend(title='Month')
plt.show()
