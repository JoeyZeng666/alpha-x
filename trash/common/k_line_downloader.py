import time
import ccxt
import pandas as pd

def fetch_kline_data(symbol, timeframe, since, before, save_path):
    # Initialize the OKX exchange
    exchange = ccxt.okx()

    # Print the time range in a human-readable format
    print(f"Fetching data from {pd.to_datetime(since, unit='ms')} to {pd.to_datetime(before, unit='ms')} ...")

    # Initialize an empty DataFrame to store the data
    all_ohlcvs = []
    count = 0
    while since < before:
        # Fetch data
        count += 1
        print(f"Fetching data since {count} ...")
        ohlcvs = exchange.fetch_ohlcv(symbol=symbol, timeframe=timeframe, since=since, limit=100)
        if not ohlcvs:
            break
        # Update since to the timestamp of the last data point + 1ms to avoid duplicates
        since = ohlcvs[-1][0] + 1
        all_ohlcvs.extend(ohlcvs)
        # Wait for a while to avoid being rate-limited
        time.sleep(exchange.rateLimit / 1000)

    # Convert all data to a DataFrame
    df = pd.DataFrame(all_ohlcvs, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

    # Convert timestamps to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Save to a CSV file
    df.to_csv(save_path, index=False)

    print(f"Data has been saved to {save_path}")

# Prompt the user for input
symbol = input("Enter the symbol (e.g., BTC/USDT): ")
timeframe = input("Enter the timeframe (e.g., 1m): ")
since = int(input("Enter the start timestamp (e.g., 1720195200000): "))
before = int(input("Enter the end timestamp (e.g., 1720281600000): "))
save_path = input("Enter the save file_path for the CSV file: ")



# Call the function to fetch and save the data
fetch_kline_data(symbol, timeframe, since, before, save_path)
