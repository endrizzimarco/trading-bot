import pandas as pd
import numpy as np
import tulipy as ti

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


# Moving averages


def SMA(closePrices, n):
    return pd.Series(closePrices).rolling(n).mean()


def EMA(closePrices, n):
    return pd.Series(closePrices).ewm(span=n).mean()


def print_info(indicator):
    print("Type:", indicator.type)
    print("Full Name:", indicator.full_name)
    print("Inputs:", indicator.inputs)
    print("Options:", indicator.options)
    print("Outputs:", indicator.outputs)


def macd(input, short, long, signal):
    macd, macd_signal, macd_histogram = ti.macd(input, short, long, signal)
    return macd

def rsi(input, n):
    rsi = ti.rsi(input, n)
    return make_same_length(rsi, n)

def make_same_length(res_array, n):
    nan_array = np.empty(n)
    nan_array[:] = np.NaN
    return np.concatenate([nan_array, res_array])