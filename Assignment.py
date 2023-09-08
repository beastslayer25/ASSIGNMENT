import pandas as pd

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('stock_prices.csv')

# Calculate the daily returns for each stock
data['Return'] = data.groupby('Stock Symbol')['Close Price'].pct_change()

# Calculate the average daily return for each stock
average_return = data.groupby('Stock Symbol')['Return'].mean()

# Calculate the maximum daily return for each stock
maximum_return = data.groupby('Stock Symbol')['Return'].max()

# Calculate the minimum daily return for each stock
minimum_return = data.groupby('Stock Symbol')['Return'].min()

# Calculate the standard deviation of the daily returns for each stock
std_deviation = data.groupby('Stock Symbol')['Return'].std()

# Print the results
print("Average Daily Return:")
print(average_return)
print("\nMaximum Daily Return:")
print(maximum_return)
print("\nMinimum Daily Return:")
print(minimum_return)
print("\nStandard Deviation of Daily Returns:")
print(std_deviation)