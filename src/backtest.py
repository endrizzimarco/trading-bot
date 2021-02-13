from endpoints.instrument import Instrument
from backtesting import Backtest
from strategies import *
import pandas as pd

"""
Backtest trading strategy on multiple time periods

@param str pair: The currency pair to test on
@param: str startDate: Start backtest from this date
@param: str endDate: End backtest on this date
@param: str granularity: Candles Granularity eg. 'M15', 'H1', 'H4', 'W', 'M'
@param: str freq:
@param: Strategy strategy: Trading strategy to use
@param: bool optimize: Whether to run optimization and show parameters that make the most money
"""


def backtest(pair, startDate, endDate, granularity, freq, strategy, optimize):
    datelist = pd.date_range(start=startDate, end=endDate, freq=freq)
    data = []
    columns = ["Start", "End", "Equity"]
    # TODO paramaters should work for every strategy
    if optimize:
        columns.extend(["n1", "n2", "Threshold"])

    # Separate input period based on frequency and run simulation on each subperiod
    for i in range(len(datelist) - 1):
        start = str(datelist[i].date())
        end = str(datelist[i + 1].date())
        candles = Instrument(
            pair, params={"from": start, "to": end, "granularity": granularity}
        ).df

        # If not weekened
        if candles is not None:
            # Run backtest
            bt = Backtest(candles, strategy, cash=100000, commission=0)
            stats = bt.run()
            row = [start, end, stats[4] - 100000]

            # Search for optimal paramteres and add them to the dataframe
            if optimize:
                stats = bt.optimize(
                    threshold=range(50, 100, 1), maximize="Equity Final [$]"
                )
                vars = stats._strategy
                row.extend([vars.n, vars.n2, vars.threshold])

            data.append(row)

    df = pd.DataFrame(data, columns=columns)
    print(df)
    print("\nTotal $$$:", df["Equity"].sum())

    # TODO make this work for any strategy
    if optimize:
        print("Best n1:", df["n1"].value_counts().idxmax())
        print("Best n2:", df["n2"].value_counts().idxmax())
        print(
            "Best threshold:",
            df["Threshold"].mean(),
            df["Threshold"].value_counts().idxmax(),
        )


backtest("EUR_USD", "2017-01-01", "2021-01-01", "H1", "M", Ichimoku, 0)


# Below is to test a single period of time without having to append all the dates
# Problem is that the API has a maximum number of candles per query

# bt = Backtest(
#     Instrument(
#         "EUR_USD",
#         params={"from": "2016-12-10", "to": "2018-02-01", "granularity": "H4"},
#     ).df,
#     Ichimoku,
#     cash=100000,
#     commission=0,
# )

# stats = bt.run()
# print(stats)
# print(stats._trades.tail(40))

# stats = bt.optimize(
#                     threshold=range(5, 50, 1),
#                     maximize='Equity Final [$]')
# print(stats._strategy)


# This if for concatenating multiple period of time without surpassing API limits

# def fetch_data(start, end, granularity, freq):
#     datelist = pd.date_range(start=start, end=end, freq=freq)
#     week = []

#     for i in range(len(datelist) - 1):
#         start = str(datelist[i].date())
#         end = str(datelist[i + 1].date())
#         week.append(
#             Instrument(
#                 "EUR_USD", params={"from": start, "to": end, "granularity": granularity}
#             ).df
#         )
#     return pd.concat(week)