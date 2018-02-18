import os

path = os.path.dirname(__file__)

CONFIG = {
    "PATH": path,
    "VERBOSE": False,
    "EXCHANGE": "poloniex",
    "PERIOD": "1d",
    "BASE": "ETH",
    "QUOTE": "BTC",
    "SEARCH_TERMS": ["bitcoin", "cryptocurrency"],
    "JPN_SEARCH_TERMS": ["ビットコイン", "暗号侵害"]
}
