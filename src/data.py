# src/data.py
import yfinance as yf
import pandas as pd


def get_data(ticker, period="1y"):
    df = yf.download(ticker, period=period, auto_adjust=True)
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    df = get_data("BTC-USD")
    print(df.tail())