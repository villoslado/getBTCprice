# Bitcoin Price Fetcher 📈

This Python script fetches the latest Bitcoin price and other data such as circulating supply, 24h trading volume, market cap, and market dominance using the CoinMarketCap API.

## Features
- Fetches current price of Bitcoin in USD.
- Retrieves circulating supply, last updated time, 24h volume, 24h volume change, market cap, and market cap dominance.
- Outputs data in a clean format.

## How To Use It

### Prerequisites
- You must have Python installed.
- You'll need an API key from [CoinMarketCap](https://coinmarketcap.com/api/) to access their API.
- The `requests` and `python-dotenv` libraries. You can install them using the following command:

```bash
pip install requests python-dotenv
```

### Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/villoslado/getBTCprice.git
   cd getBTCprice

2. **Create a .env file**:

Inside the project directory, create a `.env` file and add your CoinMarketCap API key as follows:

`CMC_API_KEY=your_api_key_here`

3. **Run the Script**:

You can run the script using Python:

```bash
python get_btc_price.py
```
