import pandas as pd

# Min and max subsequences of candles


def max_subsequence(closePrices):
    priceChange = [
        round(closePrices.iloc[i + 1] - closePrices.iloc[i], 5)
        for i in range(len(closePrices) - 1)
    ]
    maxSoFar = 0
    maxToHere = 0

    for i in range(len(priceChange)):
        maxToHere += priceChange[i]
        if maxToHere < 0:
            maxToHere = 0
        if maxSoFar < maxToHere:
            maxSoFar = maxToHere
    return int(round((maxSoFar * 10 ** 4)))


def min_subsequence(closePrices):
    priceChange = [
        round(closePrices.iloc[i + 1] - closePrices.iloc[i], 5)
        for i in range(len(closePrices) - 1)
    ]
    minSoFar = 0
    minToHere = 0

    for i in range(len(priceChange)):
        minToHere += priceChange[i]
        if minToHere > 0:
            minToHere = 0
        if minSoFar > minToHere:
            minSoFar = minToHere

    return int(round((minSoFar * 10 ** 4)))


def MAXSEQ(values, n):
    return pd.Series(values).rolling(n).apply(max_subsequence)


def MINSEQ(values, n):
    return pd.Series(values).rolling(n).apply(min_subsequence)


# For Ichimoku


def tenkanSen(df):
    period9High = pd.Series(df.High).rolling(9).max()
    perdiod9Low = pd.Series(df.Low).rolling(9).min()

    return (period9High + perdiod9Low) / 2


def kijunSen(df):
    period26High = pd.Series(df.High).rolling(26).max()
    period26Low = pd.Series(df.Low).rolling(26).min()

    return (period26High + period26Low) / 2


def senkouSpanA(df):
    return ((tenkanSen(df) + kijunSen(df)) / 2).shift(26)


def senkouSpanB(df):
    period52High = pd.Series(df.High).rolling(52).max()
    period52Low = pd.Series(df.Low).rolling(52).min()

    return ((period52High + period52Low) / 2).shift(26)


def chikouSpan(df):
    return pd.Series(df.Close).shift(-26)