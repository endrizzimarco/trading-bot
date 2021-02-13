import matplotlib.pyplot as plt
import mplfinance as mpf
from endpoints.instrument import Instrument
from indicators import *


df = Instrument(
    "EUR_USD", params={"from": "2020-9-10", "to": "2021-01-01", "granularity": "H4"}
).df

df["tenkanSen"] = tenkanSen(df)
df["kijunSen"] = kijunSen(df)
df["senkouSpanA"] = senkouSpanA(df)
df["senkouSpanB"] = senkouSpanB(df)
df["chikouSpan"] = chikouSpan(df)

indicator = df.drop(["Volume", "Open", "Close", "High", "Volume", "Low"], axis=1)

mpf.plot(
    df,
    type="candle",
    style="charles",
    title="EURUSD STUFF",
    ylabel="Price ($)",
    addplot=mpf.make_addplot(indicator),
)

plt.show()
