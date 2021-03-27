import os

import numpy as np
import pandas as pd


class DataSet:

    def __init__(self, path: str):
        self.data = pd.concat([pd.read_csv(os.path.join(path, f), usecols=[0, 1, 3]) for f in os.listdir(path)])
        self.data.sort_values(by=['Unix Timestamp'], inplace=True)

    def get_data(self, interval: int = 15):
        data = self.data.iloc[::interval, :]
        data.reset_index(inplace=True, drop=True)
        return data

    def get_training_split(self, interval: int, duration_of_episode):
        data = self.get_data(interval=interval)
        N = data.shape[0]
        dfs = np.array_split(data, N//duration_of_episode * interval)
        return dfs[0: len(dfs)//10*8], dfs[len(dfs)//10*8: ]


if __name__ == '__main__':
    dataset = DataSet('original')
    train, test = dataset.get_training_split(interval=10, duration_of_episode=600)
    print(len(train), len(test))