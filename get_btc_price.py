import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("CMC_API_KEY")
url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": API_KEY}
params = {"symbol": "BTC", "convert": "USD"}
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    btc_info = data["data"]["BTC"][0]

    name = btc_info["name"]
    circulating_supply = btc_info["circulating_supply"]
    last_updated = btc_info["last_updated"]

    quote = btc_info["quote"]["USD"]
    price = quote["price"]
    volume_24h = quote["volume_24h"]
    volume_change_24h = quote["volume_change_24h"]
    market_cap = quote["market_cap"]
    market_cap_dominance = quote["market_cap_dominance"]

    print(f"Name: {name}")
    print(f"Circulating Supply: {circulating_supply:,.0f}")
    print(f"Last Updated: {last_updated}")
    print(f"Price: ${price:,.0f}")
    print(f"24h Volume: ${volume_24h:,.0f}")
    print(f"24h Volume Change: {volume_change_24h:.1f}%")
    print(f"Market Cap: ${market_cap:,.0f}")
    print(f"Market Cap Dominance: {market_cap_dominance:.1f}%")

else:
    print(f"Error fetching data: {response.status_code}, {response.text}")
