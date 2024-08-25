# Bitcoin Price Fetcher 📈

This Python script fetches the latest Bitcoin (BTC) price and related data such as circulating supply, 24h trading volume, market capitalization, and market dominance using the CoinMarketCap API. It also formats the output to make it more readable.

## Features
- Fetches the current price of Bitcoin in USD.
- Retrieves Bitcoin's circulating supply, last updated time, 24h volume, 24h volume change, market cap, and market cap dominance.
- Outputs the data in a clean, human-readable format with formatted numbers.

## How To Run This or Use It

### Prerequisites
- You must have Python installed (preferably Python 3.x).
- You'll need an API key from [CoinMarketCap](https://coinmarketcap.com/api/) to access their API.
- The `requests` and `python-dotenv` libraries are required for the script. You can install them using the following command:

```bash
pip install requests python-dotenv
```

### Setup

1. **Clone this repository**:

   ```bash
   git clone https://github.com/villoslado/getBTCprice.git
   cd getBTCprice
