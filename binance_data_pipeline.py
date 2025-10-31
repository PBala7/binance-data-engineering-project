import requests
import pandas as pd
from datetime import datetime

# Step 1: Fetch live data from Binance public API
url = "https://api.binance.com/api/v3/ticker/24hr"
response = requests.get(url)
data = response.json()

# Step 2: Convert JSON to DataFrame
df = pd.DataFrame(data)

# Step 3: Select only useful columns
df = df[['symbol', 'lastPrice', 'priceChangePercent', 'quoteVolume']]

# Step 4: Add timestamp
df['timestamp'] = datetime.now()

# Step 5: Convert numeric columns to float
df['lastPrice'] = df['lastPrice'].astype(float)
df['priceChangePercent'] = df['priceChangePercent'].astype(float)
df['quoteVolume'] = df['quoteVolume'].astype(float)

# Step 6: Save to CSV
df.to_csv("binance_data.csv", index=False)

print("✅ Binance data saved as binance_data.csv")