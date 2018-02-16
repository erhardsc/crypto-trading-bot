import config
import pandas as pd
import sys


def main(argv):
    path = config.CONSTS["PATH"]
    indicators = pd.read_csv(path + "/data/indicators.csv")
    indicators = indicators[['date','momentum','movingAverage']]
    candlesticks = pd.read_csv(path + "/data/candlesticks.csv")
    candlesticks = candlesticks[['date','open','high','low','close','volume','weightedAverage',]]
    merged = indicators.merge(candlesticks, on='date', left_index=False, right_index=False, how="inner")
    merged.to_csv(path + '/data/merged_data.csv', index=False)



if __name__ == "__main__":
    main(sys.argv[1:])
