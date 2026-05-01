import streamlit as st
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))
# Simülasyon için eğer rsi 30'un altındaysa "BUY", 70'in üstündeyse "SELL" sinyali veriyoruz. Diğer durumlarda "HOLD" sinyali veriyoruz.
def add_signals(df, oversold=30, overbought=70):
    df["Signal"] = "HOLD"
    df.loc[df["RSI"] < oversold, "Signal"] = "BUY"
    df.loc[df["RSI"] > overbought, "Signal"] = "SELL"
    return df

from data import get_data
from indicators import calculate_rsi
from simulation import simulate

st.set_page_config(page_title="RSI Trading Bot", layout="wide")
st.title("📈 RSI Trading Bot")

col1, col2, col3 = st.columns(3)
with col1:
    ticker = st.text_input("Ticker", value="BTC-USD")
with col2:
    period = st.selectbox("Periyot", ["1mo", "3mo", "6mo", "1y"])
with col3:
    initial = st.number_input("Başlangıç ($)", value=1000)

oversold = st.slider("Oversold", 10, 40, 30)
overbought = st.slider("Overbought", 60, 90, 70)

if st.button("Analiz Et"):
    df = get_data(ticker, period)
    df = calculate_rsi(df)
    df = add_signals(df, oversold, overbought)

    last = df.iloc[-1]
    final = simulate(df, initial)
    profit = round(final - initial, 2)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("RSI", round(float(last["RSI"]), 2))
    col2.metric("Sinyal", str(last["Signal"]))
    col3.metric("Sonuç ($)", final)
    col4.metric("Kar/Zarar ($)", profit, delta=profit)

    st.subheader("Fiyat & Sinyaller")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"].squeeze(), name="Fiyat", line=dict(color="blue")))
    buys = df[df["Signal"] == "BUY"]
    sells = df[df["Signal"] == "SELL"]
    fig.add_trace(go.Scatter(x=buys.index, y=buys["Close"].squeeze(), mode="markers", name="BUY", marker=dict(color="green", size=10, symbol="triangle-up")))
    fig.add_trace(go.Scatter(x=sells.index, y=sells["Close"].squeeze(), mode="markers", name="SELL", marker=dict(color="red", size=10, symbol="triangle-down")))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("RSI")
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df.index, y=df["RSI"].squeeze(), name="RSI", line=dict(color="purple")))
    fig2.add_hline(y=oversold, line_dash="dash", line_color="green", annotation_text="Oversold")
    fig2.add_hline(y=overbought, line_dash="dash", line_color="red", annotation_text="Overbought")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Son 20 Veri")
    st.dataframe(df[["Close", "RSI", "Signal"]].tail(20))