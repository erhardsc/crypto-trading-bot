import datetime
import os


path = os.path.dirname(__file__)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

epoch = datetime.datetime.utcfromtimestamp(0)
now = unix_time_millis(datetime.datetime.now())

def create_dir(dir):
    if not os.path.exists(dir):
        return os.makedirs(dir)

CONFIG = {
    "PATH": path,
    "VERBOSE": False,
    "EXCHANGE": "poloniex",
    "START": 0,
    "END": now,
    "PAIRS": ["ETH/BTC","LTC/BTC","BTS/BTC", "STEEM/BTC"],
    "PERIOD": "1d",
    "BASE": "ETH",
    "QUOTE": "BTC",
    "SEARCH_TERMS": ["bitcoin", "cryptocurrency"],
    "JPN_SEARCH_TERMS": ["ビットコイン", "暗号侵害"]
}
