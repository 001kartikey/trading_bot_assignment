import os
from binance.client import Client

class BinanceClient:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        self.client = Client(
            api_key=api_key,
            api_secret=api_secret,
            testnet=True
        )
