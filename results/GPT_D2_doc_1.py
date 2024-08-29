import pandas as pd

# Load the CSV file to check its format and contents
file_path = '/mnt/data/on_on.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the CSV to understand its structure and content
data.head()

# Filter for rows where HTTP is used
http_data = data[(data['protocol'] == 'HTTP') & (data['request_method'].isin(['GET', 'POST']))]

# Identify potential heartbeat (GET with .js), data transfer (POST with no extension), and kill signals (GET with .png)
heartbeat_uris = http_data[http_data['request_uri'].str.contains(r'\.js$', na=False)]
data_transfer_uris = http_data[http_data['request_method'] == 'POST']
kill_signal_uris = http_data[http_data['request_uri'].str.contains(r'\.png$', na=False)]

# Count the occurrences of each type
heartbeat_count = heartbeat_uris.shape[0]
data_transfer_count = data_transfer_uris.shape[0]
kill_signal_count = kill_signal_uris.shape[0]

heartbeat_count, data_transfer_count, kill_signal_count
