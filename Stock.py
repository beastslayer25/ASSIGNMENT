import csv

# data 
stock_prices = [
    {"Date": "2023-09-01", "Stock Symbol": "AAPL", "Open Price": 150.00, "High Price": 155.00, "Low Price": 148.50, "Close Price": 152.75},
    {"Date": "2023-09-02", "Stock Symbol": "AAPL", "Open Price": 151.50, "High Price": 153.75, "Low Price": 149.50, "Close Price": 152.00},
    {"Date": "2023-09-01", "Stock Symbol": "GOOG", "Open Price": 2800.00, "High Price": 2850.00, "Low Price": 2750.00, "Close Price": 2825.50},
    {"Date": "2023-09-02", "Stock Symbol": "GOOG", "Open Price": 2830.50, "High Price": 2845.00, "Low Price": 2795.00, "Close Price": 2820.25},
]

# field names
field_names = ["Date", "Stock Symbol", "Open Price", "High Price", "Low Price", "Close Price"]

# filename
filename = "stock_prices.csv"

# data to the CSV file
with open(filename, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(stock_prices)

print(f"CSV file '{filename}' created successfully.")