import os

import pandas as pd


class DataSet:

    def __init__(self, path: str):
        self.data = pd.concat([pd.read_csv(os.path.join(path, f), usecols=[0, 1, 3]) for f in os.listdir(path)])
        self.data.sort_values(by=['Unix Timestamp'], inplace=True)

    def get_data(self, range: int = 15):
        data = self.data.iloc[::range, :]
        data.reset_index(inplace=True, drop=True)
        return data


if __name__ == '__main__':
    DataSet('original')
