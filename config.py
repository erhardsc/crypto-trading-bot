import util as util

CONFIG = {
    "PATH": util.get_path(),
    "VERBOSE": False,
    "EXCHANGE": "poloniex",
    "START": 0,
    "END": util.get_current_epoch(),
    "PAIRS": {
        "ETH/BTC": 0.4, # Portfolio allocation amount
        "LTC/BTC": 0.4,
        "BTS/BTC": 0.1,
        "STEEM/BTC": 0.1
    },
    "PERIOD": "1d",
    "BASE": "ETH",
    "QUOTE": "BTC",
    "SEARCH_TERMS": {
        "bitcoin": "ビットコイン",
        "cryptocurrency": "暗号侵害"
    }
}
