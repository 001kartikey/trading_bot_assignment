import argparse
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order(
            args.symbol,
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        client = BinanceClient().client

        response = place_order(
            client,
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        print("\nORDER REQUEST SUMMARY")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        print("\nORDER RESPONSE")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))

        print("\nSUCCESS: Order placed successfully")

    except Exception as e:
        print("FAILED:", str(e))

if __name__ == "__main__":
    main()
