# RSI Signal Bot

Basit RSI (Relative Strength Index) indikatörü kullanarak 
al/sat sinyali üreten ve simülasyon yapan trading botu.

## Ne Yapıyor?

- yfinance ile gerçek piyasa verisi çekiyor
- RSI hesaplıyor ve BUY/SELL/HOLD sinyali üretiyor
- Başlangıç sermayesiyle simülasyon yapıyor

## Sonuçlar

| Metrik | Değer |
|--------|-------|
| Strateji | RSI (14) |
| Oversold Eşiği | < 30 → BUY |
| Overbought Eşiği | > 70 → SELL |
| Test Periyodu | 1 Yıl - 6 ay - 3 ay - 1 ay|

## Teknolojiler

Python · yfinance · Pandas · Plotly · Streamlit

## Nasıl Çalıştırılır?


pip install -r requirements.txt
streamlit run app/app.py


## Demo


https://github.com/user-attachments/assets/41d8123a-c309-441c-ae05-ee8a84a7f2d2





### Açılış Sayfası
![Açılış](screenshots/acilis_sayfasi.png)

### Analiz Sonuçları
![Analiz Sonuçları](screenshots/analiz_sonuçlari.png)

### Fiyat + Sinyal Grafiği
![Fiyat Sinyal](screenshots/fiyat_sinyal_grafiği.png)

### RSI Grafiği
![RSI](screenshots/rsi_grafiği.png)

### 20 Günlük Analiz
![20 Günlük Analiz](screenshots/20_gunluk_analiz.png)
