# eğer rsi 30'un altındaysa "BUY", 70'in üstündeyse "SELL" sinyali veriyoruz. Diğer durumlarda "HOLD" sinyali veriyoruz. bu strateji uygulandıktan sonra simülasyon yaparak kar/zarar durumunu hesaplıyoruz.
def simulate(df, initial=1000):
    cash = float(initial)
    position = 0.0
    for _, row in df.iterrows():
        price = float(row["Close"].iloc[0]) if hasattr(row["Close"], 'iloc') else float(row["Close"])
        signal = str(row["Signal"].iloc[0]) if hasattr(row["Signal"], 'iloc') else str(row["Signal"])
        if signal == "BUY" and cash > 0:
            position = cash / price
            cash = 0.0
        elif signal == "SELL" and position > 0:
            cash = position * price
            position = 0.0
    final = cash if cash > 0 else position * float(df["Close"].iloc[-1])
    return round(final, 2)