from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_KEY = os.getenv("CMC_API_KEY")
url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/ohlcv/historical"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY,
}

crypto_symbol = "BTC"
convert_currencies = "USD,MXN"
yday = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")

params = {
    "symbol": crypto_symbol,
    "time_period": "daily",
    "time_start": yday,
    "time_end": yday,
    "convert": convert_currencies,
}

response = requests.get(
    url,
    headers=headers,
    params=params,
)

if response.status_code == 200:
    data = response.json()
    ohlcv_data = data["data"]["quotes"][0]["quote"]

    usd_data = ohlcv_data["USD"]
    mxn_data = ohlcv_data["MXN"]

    print(f"OHLC data for Bitcoin on {yday} in USD:")
    print(f"Close: {usd_data['close']}")
    print(f"\nOHLC data for Bitcoin on {yday} in MXN:")
    print(f"Close: {mxn_data['close']}")

else:
    print(f"Error fetching data: {response.status_code}, {response.text}")
