import matplotlib.pyplot as plt


class BotLog(object):
    def __init__(self):
        pass

    def log(self, message):
        print(message)

    def graph(self, df):
        df.plot()
        plt.show()
