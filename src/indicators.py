# src/indicators.py
import pandas as pd

# rsi hesaplama : formülü 100 - (100 / (1 + RS)) şeklindedir. RS ise ortalama kazanç / ortalama kayıp olarak hesaplanır.
def calculate_rsi(df, period=14):
    delta = df["Close"].diff() # fiyatı önceki güne göre farkını alır
    gain = delta.where(delta > 0, 0) # gain ile pozitif  farkları alırız
    loss = -delta.where(delta < 0, 0) # loss ile negatif farkları alırız ve negatif olduğu için - ile çarparız
    avg_gain = gain.rolling(period).mean() # ortalalma kazanç 14 günlük hareketli ortalama ile hesaplanır
    avg_loss = loss.rolling(period).mean() # ortalama kayıp 14 günlük hareketli ortalama ile hesaplanır
    rs = avg_gain / avg_loss # RS hesaplanır
    df["RSI"] = 100 - (100 / (1 + rs))
    return df