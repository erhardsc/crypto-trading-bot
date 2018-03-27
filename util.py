import datetime
import os

def get_path():
    return os.path.dirname(__file__)

def unix_time_millis(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0

def get_current_epoch():
    return unix_time_millis(datetime.datetime.now())

def create_dir(dir):
    if not os.path.exists(dir):
        return os.makedirs(dir)
