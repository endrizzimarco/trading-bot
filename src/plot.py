import matplotlib.pyplot as plt
import mplfinance as mpf
from endpoints.instrument import Instrument
from indicators import *


df = Instrument(
    "EUR_USD", params={"from": "2020-07-01", "to": "2020-10-02", "granularity": "H1"}
).df

# 0  -30000       103      181     1.12776    1.12998  -66.6  -0.001969 2020-07-07 11:00:00 2020-07-10 17:00:00 3 days 06:00:00
# 1   30000       183      284     1.12984    1.13878  268.2   0.007913 2020-07-10 19:00:00 2020-07-17 00:00:00 6 days 05:00:00
# 2  -30000       467      481     1.17291    1.17296   -1.5  -0.000043 2020-07-28 15:00:00 2020-07-29 05:00:00 0 days 14:00:00
# 3  -30000       511      572     1.17472    1.17601  -38.7  -0.001098 2020-07-30 11:00:00 2020-08-04 00:00:00 4 days 13:00:00
# 4   30000       580      654     1.17865    1.18170   91.5   0.002588 2020-08-04 08:00:00 2020-08-07 10:00:00 3 days 02:00:00
# 5  -30000       773      883     1.18163    1.18656 -147.9  -0.004172 2020-08-14 09:00:00 2020-08-20 23:00:00 6 days 14:00:00
# 6   30000       885      899     1.18743    1.17797 -283.8  -0.007967 2020-08-21 01:00:00 2020-08-21 15:00:00 0 days 14:00:00
# 7   30000       923      930     1.18133    1.17914  -65.7  -0.001854 2020-08-24 15:00:00 2020-08-24 22:00:00 0 days 07:00:00
# 8  -30000      1000     1117     1.18193    1.18336  -42.9  -0.001210 2020-08-27 20:00:00 2020-09-03 17:00:00 6 days 21:00:00
# 9   30000      1119     1166     1.18570    1.18160 -123.0  -0.003458 2020-09-03 19:00:00 2020-09-07 18:00:00 3 days 23:00:00
# 10  30000      1482     1496     1.16700    1.16311 -116.7  -0.003333 2020-09-24 22:00:00 2020-09-25 12:00:00 0 days 14:00:00

# yellow green brown red+purple
# tenkan kyujin lagline cloud

# green yellow price cloud
# cloud price yellow green
# df["tenkanSen"] = tenkanSen(df)
# df["kijunSen"] = kijunSen(df)
# df["senkouSpanA"] = senkouSpanA(df)
# df["senkouSpanB"] = senkouSpanB(df)
# df["chikouSpan"] = chikouSpan(df)
# df["SMA"] = SMA(df.Close, 20)
# df["EMA"] = EMA(df.Close, 20)

indicator = df.drop(["Volume", "Open", "High", "Volume", "Low"], axis=1)

mpf.plot(
    df,
    type="candle",
    style="yahoo",
    title="EURUSD STUFF",
    ylabel="Price ($)",
    addplot=mpf.make_addplot(indicator),
)

plt.show()
