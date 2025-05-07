from gs_quant.data import Dataset


# Define the stock ticker (e.g., Apple)
stock_symbol = 'AAPL'

# Create a dataset object to get time series data for the stock
dataset = Dataset('time_series', stock_symbol)

# Get data for the stock within a given date range
data = dataset.get_data(start_date='2023-01-01', end_date='2023-12-31')

# Print the data
print(data)