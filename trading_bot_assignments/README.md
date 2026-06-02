# Binance Futures Testnet Trading Bot

## Setup

1. Create Binance Futures Testnet account.
2. Generate API Key and Secret.
3. Create .env file:

API_KEY=your_key
API_SECRET=your_secret

4. Install dependencies:

pip install -r requirements.txt

## Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

## Limit Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000

## Features

- MARKET Orders
- LIMIT Orders
- BUY / SELL Support
- Logging
- Validation
- Error Handling

## Assumptions

- User has valid testnet credentials.
- Quantity and price follow Binance rules.
