import util as util

CONFIG = {
    "PATH": util.get_path(),
    "VERBOSE": False,
    "EXCHANGE": "poloniex",
    "START": 0,
    "END": util.get_current_epoch(),
    "PAIRS": {
        "ETH/USDT": 0.4, # Portfolio allocation amount
        "LTC/USDT": 0.4,
        "BTC/USDT": 0.1,
        "XMR/USDT": 0.1
    },
    "PERIOD": "1d",
    "BASE": "ETH",
    "QUOTE": "BTC",
    "SEARCH_TERMS": {
        "bitcoin": "ビットコイン",
        "cryptocurrency": "暗号侵害"
    }
}
